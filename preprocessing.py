import pandas as pd
import numpy as np


def data_import():
    train_dev = pd.read_csv("D:/rawDataFiles/housePrice_train.csv")
    test = pd.read_csv("D:/rawDataFiles/housePrice_test.csv")
    print(train_dev.describe())
    print(test.describe())

    return train_dev, test



def preprocess(train_dev, test):
    na_check(train_dev, test)




def na_check(train_dev, test):
    # Reference for feature factors at :
    # https://storage.googleapis.com/kaggle-competitions-data/kaggle/5407/data_description.txt?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com&Expires=1516070880&Signature=aRKYNWh%2FHIHQNWPpczNU3G1syEYPp%2F8Q1d0ga4GqjP3NY%2F6ZKAyImuU1flxo7Rx8cCJeeYvYGdPetCIiC1%2F9KuFedaFx6vOhLTuqq1tEcJU%2BDAc%2BG1Q6ODv86BjiqaEtCSQx%2BEqVIhDvQA9kQwXWSKbR%2Fx7BW4NdUXh0PkkX9VXs0hQxSPPubs2oiEZzuaP%2F3FQlABH46WidivszV4cYCr8Z8dscmJQ4oRh59RK0qE27AIkkPwvq8FfR5oHQumILtN04LSxpOZlsjzxv%2BCN8HE8GkPyzwUhnVGaWSrPkGp3DUpb8Ct2EkT0x7wUF92FVEw61QVTWVkn6tXsQRSre%2Fg%3D%3D

    for dataset in [train_dev, test] :
        dataset.Alley = train_dev.Alley.replace(np.nan, 'NoAlley')
        dataset.