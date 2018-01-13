import pandas as pd
from pandas import DataFrame
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import visualization as viz

def data_import():
    train_dev = pd.read_csv("D:/rawDataFiles/housePrice_train.csv")
    test = pd.read_csv("D:/rawDataFiles/housePrice_test.csv")
    print('train_dev set shape : ' , train_dev.shape)  # train_dev set shape :  (1460, 81)
    print('test set shape : ' , test.shape)            # test set shape :  (1459, 80)

    return train_dev, test



def preprocess(train_dev, test):
    high_corr, train_dev, test = na_check(train_dev, test)
    train_dev, test = add_feature(train_dev, test)
    train_dev, test = column_eliminate(high_corr, train_dev, test)

    train_dev['MSSubClass'] = str(train_dev['MSSubClass'])
    test['MSSubClass'] = str(test['MSSubClass'])
    print(train_dev.dtypes)

    train_dev_y = train_dev['SalePrice']
    del(train_dev['SalePrice'])
    train_dev_size = len(train_dev)

    all_data = pd.concat((train_dev, test)).reset_index(drop=True)
    all_data = pd.get_dummies(all_data)
    train_dev = all_data[:train_dev_size]
    train_dev = pd.concat((train_dev, train_dev_y), axis=1)
    test = all_data[train_dev_size:]

    print(train_dev.shape)  #(1460, 302)
    print(test.shape)  #(1459, 301)

    X, y, test = scale(train_dev, test)
    X_train, X_dev, y_train, y_dev = train_test_split(X, y, random_state=1)

    return X_train, X_dev, y_train, y_dev, test


def na_check(train_dev, test):
    # Reference for feature factors at :
    # https://storage.googleapis.com/kaggle-competitions-data/kaggle/5407/data_description.txt?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com&Expires=1516070880&Signature=aRKYNWh%2FHIHQNWPpczNU3G1syEYPp%2F8Q1d0ga4GqjP3NY%2F6ZKAyImuU1flxo7Rx8cCJeeYvYGdPetCIiC1%2F9KuFedaFx6vOhLTuqq1tEcJU%2BDAc%2BG1Q6ODv86BjiqaEtCSQx%2BEqVIhDvQA9kQwXWSKbR%2Fx7BW4NdUXh0PkkX9VXs0hQxSPPubs2oiEZzuaP%2F3FQlABH46WidivszV4cYCr8Z8dscmJQ4oRh59RK0qE27AIkkPwvq8FfR5oHQumILtN04LSxpOZlsjzxv%2BCN8HE8GkPyzwUhnVGaWSrPkGp3DUpb8Ct2EkT0x7wUF92FVEw61QVTWVkn6tXsQRSre%2Fg%3D%3D

    for dataset in [train_dev, test] :
        dataset.Alley = dataset.Alley.replace(np.nan, 'NoAlley')
        dataset.BsmtQual = dataset.BsmtQual.replace(np.nan, 'NoBsmt')
        dataset.BsmtCond = dataset.BsmtCond.replace(np.nan, 'NoBsmt')
        dataset.BsmtExposure = dataset.BsmtExposure.replace(np.nan, 'NoBsmt')
        dataset.BsmtFinType1 = dataset.BsmtFinType1.replace(np.nan, 'NoBsmt')
        dataset.BsmtFinType2 = dataset.BsmtFinType2.replace(np.nan, 'NoBsmt')
        dataset.FireplaceQu = dataset.FireplaceQu.replace(np.nan, 'NoFireplace')
        dataset.GarageType = dataset.GarageType.replace(np.nan, 'NoGarage')
        dataset.GarageFinish = dataset.GarageFinish.replace(np.nan, 'NoGarage')
        dataset.GarageQual = dataset.GarageQual.replace(np.nan, 'NoGarage')
        dataset.GarageCond = dataset.GarageCond.replace(np.nan, 'NoGarage')
        dataset.PoolQC = dataset.PoolQC.replace(np.nan, 'NoPool')
        dataset.Fence = dataset.Fence.replace(np.nan, 'NoFence')
        dataset.MiscFeature = dataset.MiscFeature.replace(np.nan, 'None')

    na_col_td = []
    na_col_test = []
    for dataset in [train_dev, test] :
        colnames = dataset.columns
        for col in colnames :
            if dataset[col].isnull().sum() != 0 :
                if int(dataset.shape[1]) == 81 : na_col_td.append(col)
                else : na_col_test.append(col)

    print('train_dev NA : ' + str(na_col_td))
    print('test NA : ' + str(na_col_test))
    # train_dev NA : ['LotFrontage', 'MasVnrType', 'MasVnrArea', 'Electrical', 'GarageYrBlt']
    # test NA : ['MSZoning', 'LotFrontage', 'Utilities', 'Exterior1st', 'Exterior2nd', 'MasVnrType', 'MasVnrArea', 'BsmtFinSF1',
    #            'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', 'BsmtFullBath', 'BsmtHalfBath', 'KitchenQual', 'Functional',
    #            'GarageYrBlt', 'GarageCars', 'GarageArea', 'SaleType']

    viz.na_proportion(na_col_td, na_col_test, train_dev, test)
    # features with high portion of NA : 'LotFrontage', 'GarageYrBlt'

    high_corr = correlation_check(train_dev, test)
    fill_na(train_dev, test)

    return high_corr, train_dev, test



def correlation_check(train_dev, test):
    viz.heatmap(train_dev, test)
    # ('YearBuilt', 'GarageYrBlt'), ('TotalBsmtSF', '1stFlrSF'), ('GrLivArea', 'TotRmsAbvGrd'), ('GarageCars', 'GarageArea')
    # have high correlations. One from each pair should be eliminated to prevent multicolinearity
    high_corr = [('YearBuilt', 'GarageYrBlt'), ('TotalBsmtSF', '1stFlrSF'), ('GrLivArea', 'TotRmsAbvGrd'), ('GarageCars', 'GarageArea')]

    return high_corr




def fill_na(train_dev, test):
    for dataset in [train_dev, test] :
        dataset.MSZoning = dataset.MSZoning.fillna("RL")
        dataset.LotFrontage = dataset.groupby("Neighborhood")["LotFrontage"].transform(lambda x: x.fillna(x.median()))
        dataset.Utilities = dataset.Utilities.fillna("AllPub")
        dataset.Exterior1st = dataset.Exterior1st.fillna(dataset.Exterior1st.mode()[0])
        dataset.Exterior2nd = dataset.Exterior2nd.fillna(dataset.Exterior2nd.mode()[0])
        dataset.MasVnrType = dataset.MasVnrType.fillna("None")
        dataset.MasVnrArea = dataset.MasVnrArea.fillna(0)
        dataset.BsmtFinSF1 = dataset.BsmtFinSF1.fillna(0)
        dataset.BsmtFinSF2 = dataset.BsmtFinSF2.fillna(0)
        dataset.BsmtUnfSF = dataset.BsmtUnfSF.fillna(dataset.BsmtUnfSF.median())
        dataset.TotalBsmtSF = dataset.TotalBsmtSF.fillna(dataset.TotalBsmtSF.median())
        dataset.BsmtFullBath = dataset.BsmtFullBath.fillna(0)
        dataset.BsmtHalfBath = dataset.BsmtHalfBath.fillna(0)
        dataset.KitchenQual = dataset.KitchenQual.fillna("TA")
        dataset.Functional = dataset.Functional.fillna("Typ")
        dataset.GarageYrBlt = dataset.GarageYrBlt.fillna(0)
        dataset.GarageCars = dataset.GarageCars.fillna(dataset.GarageCars.mode()[0])
        dataset.GarageArea = dataset.GarageArea.fillna(dataset.GarageArea.mode()[0])
        dataset.SaleType = dataset.SaleType.fillna("WD")
        dataset.Electrical = dataset.Electrical.fillna("SBrkr")

        count = 0
        for col in dataset.columns:
            count += dataset[col].isnull().sum()
        if count == 0 : print("no NA values remaining")
        # No more NA values are remaining in both train_dev and test sets.



def add_feature(train_dev, test) :
    for dataset in [train_dev, test] :
        dataset['TotalArea'] = dataset['LotArea'] + dataset['2ndFlrSF'] + dataset['TotalBsmtSF']
        dataset['FloorArea'] = dataset['1stFlrSF'] + dataset['2ndFlrSF'] + dataset['TotalBsmtSF']
    return train_dev, test





def column_eliminate(high_corr, train_dev, test) :
    from scipy.stats.stats import pearsonr

    for item in high_corr :
        print(item[0], pearsonr(train_dev[item[0]], train_dev['SalePrice']))
        print(item[1], pearsonr(train_dev[item[1]], train_dev['SalePrice']))
        if pearsonr(train_dev[item[0]], train_dev['SalePrice']) >= pearsonr(train_dev[item[1]], train_dev['SalePrice']) :
            del(train_dev[item[1]])
            del(test[item[1]])
        else :
            del(train_dev[item[0]])
            del(test[item[0]])

    del(train_dev['Id'])
    del(test['Id'])

    return train_dev, test



def scale(train_dev, test) :
    y = train_dev['SalePrice']
    del(train_dev['SalePrice'])
    X = train_dev

    scaler = MinMaxScaler()
    scaler.fit(X)
    X = DataFrame(scaler.transform(X))
    test = DataFrame(scaler.transform(test))

    return X, y, test