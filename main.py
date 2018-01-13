import preprocessing as pp


if __name__ == '__main__' :
    train_dev, test = pp.data_import()
    pp.preprocess(train_dev, test)