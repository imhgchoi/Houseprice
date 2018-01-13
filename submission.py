from pandas import DataFrame

def writeCSV(model_list, test, testID):
    for model in model_list :
        submission = DataFrame({'Id':testID, 'SalePrice':model[1].predict(test)})
        file_name = 'C:/Users/Froilan/Desktop/Repository/kaggleResultCSV/houseprice_' + model[0] + '.csv'
        submission.to_csv(file_name, index=False)