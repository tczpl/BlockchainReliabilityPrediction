########################################################
# predict.py
# Developer: Jieming Zhu <jmzhu@cse.cuhk.edu.hk>
# Created: 2014/2/6
# Last updated: 2014/2/6
########################################################

import numpy as np 
from numpy import linalg as LA
import time
from utilities import *
from UIPCC import *
from HBRP import *


########################################################
# Function to run the [UMEAN, IMEAN, UPCC, IPCC, UIPCC] 
# methods at each density
# 

def predict(matrix, density, para):

    startTime = time.perf_counter()
    numService = matrix.shape[1] 
    numUser = matrix.shape[0] 
    rounds = para['rounds']
    logger.info('Data matrix size: %d clients * %d peers'%(numUser, numService))
    logger.info('Run for %d rounds: matrix density = %.2f.'%(rounds, density))
    evalResults = np.zeros((6, rounds, len(para['metrics']))) 
    timeResults = np.zeros((6, rounds))

    inmatrix1 = np.loadtxt(para['dataPath1']) 
    inmatrix2 = np.loadtxt(para['dataPath2']) 
    inmatrix3 = np.loadtxt(para['dataPath3']) 
        
    for k in range(rounds):
        logger.info('----------------------------------------------')
        logger.info('%d-round starts.'%(k + 1))
        logger.info('----------------------------------------------')

        # load the training data, i.e., removed matrix
        trainIndicatorMatrix,testIndicatorMatrix = removeEntries(np.ones((numUser, numService)), density, k)
        (trainVecX, trainVecY) = np.where(trainIndicatorMatrix)
        trainMatrix = matrix * trainIndicatorMatrix

        (testVecX, testVecY) = np.where(testIndicatorMatrix)
        realVec = matrix[testVecX, testVecY]
        


        ## UMEAN
        iterStartTime1 = time.perf_counter()            
        predMatrixUMEAN = UMEAN(trainMatrix)     
        timeResults[0, k] = time.perf_counter() - iterStartTime1
        predVecUMEAN = predMatrixUMEAN[testVecX, testVecY]       
        evalResults[0, k, :] = errMetric(realVec, predVecUMEAN, para['metrics'])
        logger.info('UMEAN done.')

        ## IMEAN
        iterStartTime2 = time.perf_counter()          
        predMatrixIMEAN = IMEAN(trainMatrix)      
        timeResults[1, k] = time.perf_counter() - iterStartTime2
        predVecIMEAN = predMatrixIMEAN[testVecX, testVecY]    
        evalResults[1, k, :] = errMetric(realVec, predVecIMEAN, para['metrics'])
        logger.info('IMEAN done.')

        ## UPCC
        iterStartTime3 = time.perf_counter()         
        predMatrixUPCC = UPCC(trainMatrix, predMatrixUMEAN, para)  
        timeResults[2, k] = time.perf_counter() - iterStartTime3 + timeResults[0, k]
        predVecUPCC = predMatrixUPCC[testVecX, testVecY]   
        evalResults[2, k, :] = errMetric(realVec, predVecUPCC, para['metrics'])
        logger.info('UPCC done.')
        
        ## IPCC
        iterStartTime4 = time.perf_counter()         
        predMatrixIPCC = IPCC(trainMatrix, predMatrixIMEAN, para) 
        timeResults[3, k] = time.perf_counter() - iterStartTime4 + timeResults[1, k]
        predVecIPCC = predMatrixIPCC[testVecX, testVecY]
        evalResults[3, k, :] = errMetric(realVec, predVecIPCC, para['metrics'])
        logger.info('IPCC done.')

        ## UIPCC
        iterStartTime5 = time.perf_counter()       
        predMatrixUIPCC = UIPCC(trainMatrix, predMatrixUPCC, predMatrixIPCC, para)  
        timeResults[4, k] = time.perf_counter() - iterStartTime5\
                + timeResults[2, k] + timeResults[3, k]
        predVecUIPCC = predMatrixUIPCC[testVecX, testVecY]
        evalResults[4, k, :] = errMetric(realVec, predVecUIPCC, para['metrics'])
        logger.info('UIPCC done.')


        ## HBRP
        iterStartTime6 = time.perf_counter()
        intrainmatrix1 = inmatrix1 * trainIndicatorMatrix
        intrainmatrix2 = inmatrix2 * trainIndicatorMatrix
        intrainmatrix3 = inmatrix3 * trainIndicatorMatrix

        predVecHBRP = HBRP(trainMatrix, intrainmatrix1,intrainmatrix2,intrainmatrix3,  trainVecX,trainVecY,testVecX,testVecY,para)#,realVec)#realVec to watchList
        timeResults[5, k] = time.perf_counter() - iterStartTime6
        evalResults[5, k, :] = errMetric(realVec, predVecHBRP, para['metrics'])
        logger.info('HBRP done.')

        

        logger.info('%d-round done. Running time: %.2f sec'
                %(k + 1, time.perf_counter() - iterStartTime1))
        logger.info('----------------------------------------------')

    outFile = '%s%.2f.txt'%(para['outPath'], density)
    saveResult(outFile, evalResults, timeResults, para)
    logger.info('Config density = %.2f done. Running time: %.2f sec'
            %(density, time.perf_counter() - startTime))
    logger.info('==============================================')
########################################################


########################################################
# Function to compute the evaluation metrics
# Return an array of metric values
#
def errMetric(realVec, predVec, metrics):
    result = []
    absError = np.absolute(predVec - realVec) 
    mae = np.average(absError)
    for metric in metrics:
        if 'MAE' == metric:
            result = np.append(result, mae)
        if 'NMAE' == metric:
            nmae = mae / np.average(realVec)
            result = np.append(result, nmae)
        if 'RMSE' == metric:
            rmse = LA.norm(absError) / np.sqrt(absError.size)
            result = np.append(result, rmse)
        if 'MRE' == metric or 'NPRE' == metric:
            relativeError = absError / realVec
            if 'MRE' == metric:
                mre = np.percentile(relativeError, 50)
                result = np.append(result, mre)
            if 'NPRE' == metric:
                npre = np.percentile(relativeError, 90)
                result = np.append(result, npre)
    return result
########################################################