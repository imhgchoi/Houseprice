from pandas import DataFrame
import math

def writeCSV(model_list, test, testID):
    for model in model_list :
        submission = DataFrame({'Id':testID, 'SalePrice':list(map(math.exp, model[1].predict(test)))})
        file_name = 'C:/Users/Froilan/Desktop/Repository/kaggleResultCSV/houseprice_' + model[0] + '.csv'
        submission.to_csv(file_name, index=False)


def stack_writeCSV(model_list, stack, test, testID):
    test_X = DataFrame({'RID':model_list[0][1].predict(test), 'KRR':model_list[1][1].predict(test),
                        'ANN':model_list[2][1].predict(test), 'RF':model_list[3][1].predict(test)})
    submission = DataFrame({'Id':testID, 'SalePrice':list(map(math.exp, stack[1].predict(test_X)))})

    file_name = 'C:/Users/Froilan/Desktop/Repository/kaggleResultCSV/houseprice_' + stack[0] + '.csv'
    submission.to_csv(file_name, index=False)