import preprocessing as pp
import modeling as md
import submission as sb


if __name__ == '__main__' :
    train_dev, test = pp.data_import()
    test_ID = test['Id']
    X_train, X_dev, y_train, y_dev, test = pp.preprocess(train_dev, test)
    model_list = md.model(X_train, X_dev, y_train, y_dev)
    sb.writeCSV(model_list, test, test_ID)