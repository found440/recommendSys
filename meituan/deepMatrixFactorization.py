# -*- coding: utf-8 -*-

import keras
import numpy as np
import pandas as pd
import scipy
from scipy import sparse
from scipy.sparse import sparsetools
from scipy.sparse import linalg as la
import time
import math
import cPickle
import os

dataDir = '../../data/'
trainFileName = 'meituanWithId'

uidIndexs = getUidIndexs()
iidIndexs = getIidIndexs()
maxUid = len(uidIndexs)
maxIid = len(iidIndexs)

def getUidIndexs():
    postfix = '_uidIndexs.pkl'
    filename = dataDir + trainFileName+ postfix
    uidIndexs = cPickle.load(open(filename, 'r'))
    return uidIndexs

def getIidIndexs():
    postfix = '_iidIndexs.pkl'
    filename = dataDir + trainFileName+ postfix
    iidIndexs = cPickle.load(open(filename, 'r'))
    reutrn iidIndexs

def getTrainSparseMat():
    postfix = '_sparseMat.pkl'
    filename = dataDir + trainFileName+ postfix
    
    if os.path.exists(filename):
        sparseMat = cPickle.load(open(filename, 'r'))
        return sparseMat
    else:
        sparseMat = sparse.dok_matrix((maxUid, maxIid))
        sparseMatOut = file(dataDir + trainFileName.split('.')[0]+ '_sparseMat.csv', 'wb')
        reader = csv.reader(sparseMatOut)
        for keys, value in reader:
            keyI, keyJ, = keys.split(',')[0][1:], keys.split(',')[1][1:-1]
            sparseMat[int(keyI), int(keyJ)] = value

        return sparseMat


def lossFunc(sparseMat, y_predict):
    sumRes = 0
    for value in sparseMat.keys():
        yijDivideMaxR = sparseMat[value] / maxR
        yij_pre = y_predict[value]
        sumRes = yijDivideMaxR * math.log(yij_pre) + (1 - yijDivideMaxR) * math.log(1 - yij_pre)
    
    return -sumRes


def createModel():
    pass



if __name__ == '__main__':
    
    pass

