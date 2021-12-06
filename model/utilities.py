########################################################
# utilities.py
# This is a script containing a bag of useful utilities.
# Developer: Jieming Zhu <jmzhu@cse.cuhk.edu.hk>
# Created: 2014/2/6
# Last updated: 2014/2/6
########################################################


import os, sys, time
import numpy as np
import logging
import random

## global
logger = logging.getLogger('logger')   


########################################################
# Config the working paths and set up logger
#
def initConfig(para):
    config = {'exeFile': os.path.basename(sys.argv[0]),  
              'workPath': os.path.abspath('.'),
              'srcPath': os.path.abspath('src/'),
              'dataPath': os.path.abspath('../data/'),
              'logFile': os.path.basename(sys.argv[0]) + '.log'}

    # delete old log file
    if os.path.exists(config['logFile']):
        os.remove(config['logFile'])
    # add result folder
    if not os.path.exists('result'):
        os.mkdir('result')

    ## set up logger to record runtime info
    if para['debugMode']:  
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO) 
    # log to console
    cmdhandler = logging.StreamHandler()  
    cmdhandler.setLevel(logging.DEBUG)       
    formatter = logging.Formatter(
        '%(asctime)s: %(message)s')
    cmdhandler.setFormatter(formatter)
    logger.addHandler(cmdhandler)   
    # log to file
    if para['saveLog']:
        filehandler = logging.FileHandler(config['logFile']) 
        filehandler.setLevel(logging.DEBUG)
        filehandler.setFormatter(formatter)       
        logger.addHandler(filehandler)  
    
    logger.info('==========================================')
    if para['debugMode']:  
        para['rounds'] = 1
        logger.debug('Debug mode open: set rounds = 1')
    logger.info('Config:')
    config.update(para)
    for name in config:
        logger.info('%s = %s'%(name, config[name]))
########################################################
 

########################################################
# Save the evaluation results into file
#

def outputstr(array):
    res = ""
    for i in array:
        res += ("%.4f" % i)+"\t"
    return res+"\n";

def saveResult(outfile, result, timeinfo, para):
    approach = ['UMEAN\n', 'IMEAN\n', 'UPCC\n', 'IPCC\n', 'UIPCC\n', 'BPDREAM\n']
    fileID = open(outfile, 'w')
    fileID.write('Metric: ')
    for metric in para['metrics']:
        fileID.write('| %s\t'%metric)
    fileID.write('\n==========================================\n')
    for i in range(6):
        fileID.write(approach[i])
        avgResult = np.average(result[i, :, :], axis = 0)         
        fileID.write('Avg:\t')
        fileID.write(outputstr(avgResult))
        stdResult = np.std(result[i, :, :], axis = 0)
        fileID.write('Std:\t')
        fileID.write(outputstr(stdResult))
        fileID.write('==========================================\n')
    fileID.write('\n\n')

    if para['saveTimeInfo']:
        fileID = open(outfile + '_time.txt', 'w')
        fileID.write('Running time:\n')
        fileID.write('==========================================\n')
        for i in range(6):
            fileID.write(approach[i])
            fileID.write('Avg:\t%.4f\n'%np.average(timeinfo[i, :]))
            fileID.write('Std:\t%.4f\n'%np.std(timeinfo[i, :]))
            fileID.write('==========================================\n')

        fileID.write('\n\nDetailed results for %d rounds:\n'%timeinfo.shape[1])
        fileID.write('==========================================')
        for i in range(6):
            fileID.write('\n')
            fileID.write(approach[i])
            fileID.write('==========================================\n')           
            np.savetxt(fileID, np.matrix(timeinfo[i, :]).T, fmt='%.4f')
        fileID.close()
########################################################

def removeEntries(matrix, density, seedId):
    (vecX, vecY) = np.where(matrix > 0)
    vecXY = np.c_[vecX, vecY]
    numRecords = vecX.size
    numAll = matrix.size
    random.seed(seedId)
    randomSequence = list(range(0, numRecords))
    random.shuffle(randomSequence)
    numTrain = int(numAll * density)
    # by default, we set the remaining QoS records as testing data                     
    numTest = numRecords - numTrain
    trainXY = vecXY[randomSequence[0 : numTrain], :]
    testXY = vecXY[randomSequence[- numTest :], :]

    trainMatrix = np.zeros(matrix.shape)
    trainMatrix[trainXY[:, 0], trainXY[:, 1]] = matrix[trainXY[:, 0], trainXY[:, 1]]
    testMatrix = np.zeros(matrix.shape)
    testMatrix[testXY[:, 0], testXY[:, 1]] = matrix[testXY[:, 0], testXY[:, 1]]

    # ignore invalid testing data
    idxX = (np.sum(trainMatrix, axis=1) == 0)
    testMatrix[idxX, :] = 0
    idxY = (np.sum(trainMatrix, axis=0) == 0)
    testMatrix[:, idxY] = 0
    return trainMatrix, testMatrix