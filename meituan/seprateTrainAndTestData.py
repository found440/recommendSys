# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import scipy
from scipy import sparse
from scipy.sparse import sparsetools
from scipy.sparse import linalg as la
import random
import math
import cPickle
import time

dataDir = '../../data/'
trainFileName = 'meituanWithId.csv'
# trainData = pd.read_csv(dataDir + trainFileName, header=None, names=['uid', 'iid', 'score', 'time'])

uidIndexs = cPickle.load(open(dataDir + trainFileName.split('.')[0]+ '_uidIndexs.pkl', 'r'))
iidIndexs = cPickle.load(open(dataDir + trainFileName.split('.')[0]+ '_iidIndexs.pkl', 'r'))
maxUid = len(uidIndexs)
maxIid = len(iidIndexs)

#通过留一法获取train和test集合
def separateTrainAndTest(neg_ratio = 5.0):
    print "start createSparseMat"
    time0 = time.time()
    sparseMat = cPickle.load(open(dataDir + trainFileName.split('.')[0]+ '_sparseMatp.pkl', 'r'))
    positiveCount = len(sparseMat.keys())
    

    testMat = sparse.dok_matrix((maxUid, maxIid))

    count = 1
    for value in sparseMat.keys():
        count = count + 1
        if count%10 == 0:
            testMat[value] = sparseMat[value]
            #print testMat[value]
            sparseMat[value] = 0

    print "separateTrainAndTest success"
    time1 = time.time()
    print time1 - time0

    trainMatOut = open(dataDir + trainFileName.split('.')[0]+ '_trainMat.pkl', 'wb')
    cPickle.dump(sparseMat, trainMatOut)

    testMatOut = open(dataDir + trainFileName.split('.')[0]+ '_testMat.pkl', 'wb')
    cPickle.dump(testMat, testMatOut)
    

if __name__ == '__main__':
    time0 = time.time()
    separateTrainAndTest()
    #mapIndex()
    time1 = time.time()
    print time1 - time0
    pass

