from sklearn.linear_model import Ridge
from sklearn.kernel_ridge import KernelRidge
from sklearn.neural_network import MLPRegressor
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


def model(X_train, X_dev, y_train, y_dev):
    RID = RIDGE(X_train, X_dev, y_train, y_dev)
    KRR = KernelRIDGE(X_train, X_dev, y_train, y_dev)
    ANN = NEURALNET(X_train, X_dev, y_train, y_dev)

    return [('ridge', RID), ('kernel_ridge', KRR), ('neural_network', ANN)]



def RIDGE(X_train, X_dev, y_train, y_dev):
    RANDOM_STATE = 1
    MAX_ITER = 5000000
    ALPHA = [0.0001, 0.0003, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10]

    ALPHA = [3.0]

    for alpha in ALPHA :
        RID = Ridge(
            alpha = alpha,
            max_iter = MAX_ITER,
            random_state = RANDOM_STATE
        )
        RID.fit(X_train, y_train)
        train_prediction = RID.predict(X_train)
        dev_prediction = RID.predict(X_dev)
        train_prediction[train_prediction < 0] = 0
        dev_prediction[dev_prediction < 0] = 0
        train_score = rmsle(train_prediction, y_train)
        dev_score = rmsle(dev_prediction, y_dev)

        print('-------RIDGE : alpha = '+str(alpha)+'--------')
        print("train set RMSLE : ", str(round(train_score,4)))
        print("dev set RMSLE   : ", str(round(dev_score,4)))

    return RID


def KernelRIDGE(X_train, X_dev, y_train, y_dev):
    KERNEL = 'polynomial'
    DEGREE = 2
    ALPHA = [0.0001, 0.0003, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10]

    ALPHA = [3.0]

    for alpha in ALPHA :
        KRR = KernelRidge(
            alpha = alpha,
            kernel = KERNEL,
            degree = DEGREE
        )
        KRR.fit(X_train, y_train)
        train_prediction = KRR.predict(X_train)
        dev_prediction = KRR.predict(X_dev)
        train_score = rmsle(train_prediction, y_train)
        dev_score = rmsle(dev_prediction, y_dev)

        print('-------KERNEL_RIDGE : alpha = '+str(alpha)+'--------')
        print("train set RMSLE : ", str(round(train_score,4)))
        print("dev set RMSLE   : ", str(round(dev_score,4)))

    return KRR


def NEURALNET(X_train, X_dev, y_train, y_dev):
    STRUCTURE = (100, 100)
    ACTIVATION = 'relu'
    ALPHA = [0.0001, 0.0003, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10]
    SOLVER = 'adam'
    BATCH_SIZE = 200
    MAX_ITER = 5000000
    RANDOM_STATE = 1

    ALPHA = [0.0001]

    for alpha in ALPHA:
        ANN = MLPRegressor(
            alpha = alpha,
            hidden_layer_sizes = STRUCTURE,
            activation = ACTIVATION,
            solver = SOLVER,
            batch_size = BATCH_SIZE,
            max_iter = MAX_ITER,
            random_state = RANDOM_STATE
        )
        ANN.fit(X_train, y_train)
        train_prediction = ANN.predict(X_train)
        dev_prediction = ANN.predict(X_dev)
        train_score = rmsle(train_prediction, y_train)
        dev_score = rmsle(dev_prediction, y_dev)

        print('-------ANN : alpha = ' + str(alpha) + '--------')
        print("train set RMSLE : ", str(round(train_score, 4)))
        print("dev set RMSLE   : ", str(round(dev_score, 4)))

    return ANN