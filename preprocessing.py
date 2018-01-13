import pandas as pd
import numpy as np
import visualization as viz

def data_import():
    train_dev = pd.read_csv("D:/rawDataFiles/housePrice_train.csv")
    test = pd.read_csv("D:/rawDataFiles/housePrice_test.csv")
    print('train_dev set shape : ' , train_dev.shape)  # train_dev set shape :  (1460, 81)
    print('test set shape : ' , test.shape)            # test set shape :  (1459, 80)

    return train_dev, test



def preprocess(train_dev, test):
    na_check(train_dev, test)




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