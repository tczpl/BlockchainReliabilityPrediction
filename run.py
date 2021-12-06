#########################################################
# Please use Python3.
# Implemented approaches: [UMEAN, IMEAN, UPCC, IPCC, UIPCC, H-BRP]
# Evaluation metrics: MAE, NMAE, RMSE, MRE, NPRE
# Some codes of UIPCCC are from WS-DREAM (Micheal R lyu, Zibin Zheng, Jieming Zhu, Pinjia He, et al.).
#########################################################

import numpy as np
import os, sys, time
sys.path.append('model')
from utilities import *
from predict import *

def run(MaxBlockBack, MaxRtt):
    #########################################################
    # config area
    #
    para = {'dataPath': './full_matrix/SuccessRate_'+str(MaxBlockBack)+'_'+str(MaxRtt)+'.csv',
            'dataPath1':  './full_matrix/rightBlock_'+str(MaxBlockBack)+'_'+str(MaxRtt)+'.csv',
            'dataPath2':  './full_matrix/recentHeight_'+str(MaxBlockBack)+'_'+str(MaxRtt)+'.csv',
            'dataPath3':  './full_matrix/roundtripTime_'+str(MaxBlockBack)+'_'+str(MaxRtt)+'.csv',
            'outPath': './result/run_'+str(MaxBlockBack)+'_'+str(MaxRtt)+'_',
            'metrics': ['MAE', 'NMAE', 'RMSE'],#, 'MRE', 'NPRE'], # delete where appropriate
            # matrix density
            'density': [0.3, 0.5, 0.65, 0.8, 0.95],  
            'rounds': 1, # how many runs are performed at each matrix density
            'topK': 3, # the parameter of TopK similar users or services, the default value is
                        # topK = 10 as in the reference paper
            'lambda': 0.1, # the combination coefficient of UPCC and IPCC, the default value is 
                        # lambda = 0.1 as in the reference paper
            'saveTimeInfo': False, # whether to keep track of the running time
            'saveLog': False, # whether to save log into file
            'debugMode': False # whether to record the debug info
            }

    initConfig(para)
    #########################################################

    startTime = time.perf_counter() # start timing
    logger.info('==============================================')

    logger.info('[UMEAN, IMEAN, UPCC, IPCC, UIPCC, BPDREAM]')
    logger.info('Load data: %s'%para['dataPath'])
    matrixLoaded = np.loadtxt(para['dataPath']) 

    # run for each density
    for density in para['density']:
        predict(matrixLoaded, density, para)

run(0, 1000)
run(12, 1000)
run(12, 2000)
run(100, 5000)

logger.info(time.strftime('Total running time: %d-th day - %Hhour - %Mmin - %Ssec.',
         time.gmtime(time.perf_counter() - startTime)))
logger.info('==============================================')
sys.path.remove('models')