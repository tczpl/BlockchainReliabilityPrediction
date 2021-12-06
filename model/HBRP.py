import pandas as pd
import numpy as np
from scipy import  stats

import matplotlib.pyplot as plt  
import xgboost as xgb
from UIPCC import *

def HBRP(trainMatrix, intrainmatrix1,intrainmatrix2,intrainmatrix3,  trainVecX,trainVecY,testVecX,testVecY,para):

    trainVec = trainMatrix[trainVecX, trainVecY]
    intrainVec1 = intrainmatrix1[trainVecX, trainVecY]
    intrainVec2 = intrainmatrix2[trainVecX, trainVecY]
    intrainVec3 = intrainmatrix3[trainVecX, trainVecY]
    intestVec1 = IPCC(intrainmatrix1, IMEAN(intrainmatrix1), para)[testVecX, testVecY]
    intestVec2 = IMEAN(intrainmatrix2)[testVecX, testVecY]
    intestVec3 = UIPCC(intrainmatrix3, UPCC(intrainmatrix3, UMEAN(intrainmatrix3), para) , IPCC(intrainmatrix3, IMEAN(intrainmatrix3), para), para)[testVecX, testVecY]

    feature_train = pd.DataFrame({'rightBlock':intrainVec1,'recentHeight':intrainVec2,'subTime':intrainVec3})
    sr_train = pd.DataFrame(trainVec)
    feature_test = pd.DataFrame({'rightBlock':intestVec1,'recentHeight':intestVec2, 'subTime':intestVec3})
    #sr_test = pd.DataFrame(realVec)
    params = {"objective": "reg:linear",  
              "booster": "gbtree",  
              "eta": 0.05,  
              "max_depth": 500,
              "subsample": 0.05,
              "colsample_bytree": 0.7,  
              "silent": 1,  
              "seed": 800,
              "verbosity": 0
              }  
    num_boost_round = 500

    trainDF = xgb.DMatrix(feature_train, sr_train)
    testDF = xgb.DMatrix(feature_test)#,sr_test)

    #watchlist = [(trainDF, 'train'), (testDF, 'eval')]  
    gbm = xgb.train(params, trainDF, num_boost_round, verbose_eval=False)# evals=watchlist,  verbose_eval=True)  

    pre = gbm.predict(testDF)

    return pre

