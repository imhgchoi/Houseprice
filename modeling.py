from sklearn.linear_model import Ridge
from sklearn.kernel_ridge import KernelRidge
from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import RandomForestRegressor
import math
import numpy as np
from pandas import DataFrame
import evaluation as ev



def model(X_train, X_dev, y_train, y_dev):
    RID = RIDGE(X_train, X_dev, y_train, y_dev)
    KRR = KernelRIDGE(X_train, X_dev, y_train, y_dev)
    ANN = NEURALNET(X_train, X_dev, y_train, y_dev)
    RF = RANDOMFOREST(X_train, X_dev, y_train, y_dev)
    MLPstack = MLPSTACK(X_train, X_dev, y_train, y_dev, RID, KRR, ANN, RF)

    return [('ridge', RID), ('kernel_ridge', KRR), ('neural_network', ANN), ('rf', RF)], ('mlp_stack', MLPstack)





def RIDGE(X_train, X_dev, y_train, y_dev):
    RANDOM_STATE = None
    MAX_ITER = 5000000
    ALPHA = [0.00001, 0.00003, 0.0001, 0.0003, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30, 100, 300, 1000]

    ALPHA = [3, 7, 10, 13, 17]

    ALPHA = [6,7,8]

    ALPHA = [2]

    for hyper in ALPHA :
        RID = Ridge(
            alpha = hyper,
            max_iter = MAX_ITER,
            random_state = RANDOM_STATE
        )
        RID.fit(X_train, y_train)
        ev.evaluate(RID, 'RID', 'alpha', hyper, X_train, X_dev, y_train, y_dev)
    print(" ")
    return RID


def KernelRIDGE(X_train, X_dev, y_train, y_dev):
    KERNEL = 'polynomial'
    DEGREE = 2
    ALPHA = [0.00001, 0.00003, 0.0001, 0.0003, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30, 100, 300, 1000]

    ALPHA = [0.03, 0.05, 0.1, 0.15, 0.3]

    ALPHA = [0.05, 0.1, 0.2]

    ALPHA = [0.02]

    for hyper in ALPHA :
        KRR = KernelRidge(
            alpha = hyper,
            kernel = KERNEL,
            degree = DEGREE,
        )
        KRR.fit(X_train, y_train)
        ev.evaluate(KRR, 'KERNEL_RID', 'alpha', hyper, X_train, X_dev, y_train, y_dev)
    print(" ")
    return KRR


def NEURALNET(X_train, X_dev, y_train, y_dev):
    STRUCTURE = (100, 100)
    ACTIVATION = 'relu'
    ALPHA = [0.00001, 0.00003, 0.0001, 0.0003, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30, 100, 300, 1000]
    SOLVER = 'adam'
    BATCH_SIZE = 200
    MAX_ITER = 5000000
    RANDOM_STATE = None

    ALPHA = [3, 6, 10, 14, 17]

    ALPHA = [8, 10, 12]

    ALPHA = [12]

    for hyper in ALPHA:
        ANN = MLPRegressor(
            alpha = hyper,
            hidden_layer_sizes = STRUCTURE,
            activation = ACTIVATION,
            solver = SOLVER,
            batch_size = BATCH_SIZE,
            max_iter = MAX_ITER,
            random_state = RANDOM_STATE
        )
        ANN.fit(X_train, y_train)
        ev.evaluate(ANN, 'ANN', 'alpha', hyper, X_train, X_dev, y_train, y_dev)
    print(" ")
    return ANN


def RANDOMFOREST(X_train, X_dev, y_train, y_dev):
    N_ESTIMATORS = 3000
    MAX_DEPTH = [3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    MAX_FEATURES = 0.5
    N_JOBS = -1
    RANDOM_STATE = None

    MAX_DEPTH = [3,4,5]

    MAX_DEPTH = [4]

    for hyper in MAX_DEPTH:
        RF = RandomForestRegressor(
            n_estimators = N_ESTIMATORS,
            max_depth = hyper,
            max_features = MAX_FEATURES,
            n_jobs = N_JOBS,
            random_state = RANDOM_STATE
        )
        RF.fit(X_train, y_train)
        ev.evaluate(RF, 'RF', 'max_depth', hyper, X_train, X_dev, y_train, y_dev)
    print(" ")
    return RF


def MLPSTACK(X_train, X_dev, y_train, y_dev, RID, KRR, ANN, RF):
    rid_train_pred = RID.predict(X_train)
    krr_train_pred = KRR.predict(X_train)
    ann_train_pred = ANN.predict(X_train)
    rf_train_pred = RF.predict(X_train)
    rid_dev_pred = RID.predict(X_dev)
    krr_dev_pred = KRR.predict(X_dev)
    ann_dev_pred = ANN.predict(X_dev)
    rf_dev_pred = RF.predict(X_dev)

    X_train = DataFrame({'RID':rid_train_pred, 'KRR':krr_train_pred, 'ANN':ann_train_pred, 'RF':rf_train_pred})
    X_dev = DataFrame({'RID':rid_dev_pred, 'KRR':krr_dev_pred, 'ANN':ann_dev_pred, 'RF':rf_dev_pred})


    STRUCTURE = (20,20)
    ACTIVATION = 'relu'
    ALPHA = [0.00001, 0.00003, 0.0001, 0.0003, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30, 100, 300, 1000]
    SOLVER = 'adam'
    BATCH_SIZE = 200
    MAX_ITER = 5000000
    RANDOM_STATE = 2

    ALPHA = [10, 20, 30, 40, 50]

    ALPHA = [30]

    for hyper in ALPHA :
        MLPstack = MLPRegressor(
            alpha=hyper,
            hidden_layer_sizes=STRUCTURE,
            activation=ACTIVATION,
            solver=SOLVER,
            batch_size=BATCH_SIZE,
            max_iter=MAX_ITER,
            random_state=RANDOM_STATE
        )
        MLPstack.fit(X_train, y_train)
        ev.evaluate(MLPstack, 'MLPstack', 'alpha', hyper, X_train, X_dev, y_train, y_dev)

    return MLPstack