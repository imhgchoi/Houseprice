import numpy as np
import math

def rmsle(prediction, y):
    y = list(y)
    prediction = list(prediction)
    tmp = 0
    for i in range(len(prediction)):
        if prediction[i]>0 :
            tmp += (math.log(prediction[i]) - math.log(y[i]))**2
        else :
            tmp += (1 - math.log(y[i]))**2
    return math.sqrt(tmp/len(prediction))

def evaluate(MODEL, MODEL_name, hyperparam, hyper, X_train, X_dev, y_train, y_dev):
    y_train = np.array([math.exp(x) for x in y_train])
    y_dev = np.array([math.exp(x) for x in y_dev])
    train_prediction = MODEL.predict(X_train)
    dev_prediction = MODEL.predict(X_dev)
    train_prediction = np.array([math.exp(x) for x in train_prediction])
    dev_prediction = np.array([math.exp(x) for x in dev_prediction])
    train_score = rmsle(train_prediction, y_train)
    dev_score = rmsle(dev_prediction, y_dev)

    print('-------' + MODEL_name + ' : ' + hyperparam + " = " + str(hyper) + '--------')
    print("train set RMSLE : ", str(round(train_score, 4)))
    print("dev set RMSLE   : ", str(round(dev_score, 4)))
    print("difference : ", str(round(dev_score - train_score, 4)))


