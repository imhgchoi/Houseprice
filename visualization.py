import matplotlib.pyplot as plt
import seaborn as sns
from pandas import DataFrame
sns.set_style('whitegrid')
color = sns.color_palette()

def na_proportion(na_col_td, na_col_test, train_dev, test) :
    na_col = list(set(na_col_td) | set(na_col_test))

    tmp = []
    for col in na_col :
        tmp.append([(train_dev[col].isnull().sum() + test[col].isnull().sum()) / (len(train_dev) + len(test)) * 100, col])
        tmp = sorted(tmp, reverse=True)

    x = []
    y = []
    for item in tmp:
        x.append(item[1])
        y.append(item[0])

    plt.subplots(figsize=(10,10))
    plt.xticks(rotation='45')
    sns.barplot(x,y)
    plt.xlabel('Features', fontsize=15)
    plt.ylabel('Percent of missing values (%)', fontsize=15)
    plt.title('Missing Data Percentage of Features', fontsize=18)

    plt.savefig('D:/SourceCodes/github/Houseprice/visualizationResults/NAportion.png')
    plt.close()

def heatmap(train_dev, test) :
    corrmat = train_dev.corr()
    plt.subplots(figsize=(8,8))
    plt.title('train_dev Correlation Heatmap', fontsize=18)
    sns.heatmap(corrmat, vmax=0.85, square=True)
    plt.savefig('D:/SourceCodes/github/Houseprice/visualizationResults/train_dev_heatmap.png')

    corrmat = test.corr()
    plt.subplots(figsize=(8,8))
    plt.title('test Correlation Heatmap', fontsize=18)
    sns.heatmap(corrmat, vmax=0.85, square=True)
    plt.savefig('D:/SourceCodes/github/Houseprice/visualizationResults/test_heatmap.png')

    plt.close()