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
import csv

dataDir = '../../data/'
trainFileName = 'meituanWithId.csv'
trainData = pd.read_csv(dataDir + trainFileName, header=None, names=['uid', 'iid', 'score', 'time'])


activationFunc = 'ReLU'
maxR = 5.0
mu = 1.0e-6


def lossFunc(sparseMat, y_predict):
    sumRes = 0
    for value in sparseMat.keys():
        yijDivideMaxR = sparseMat[value] / maxR
        yij_pre = y_predict[value]
        sumRes = yijDivideMaxR * math.log(yij_pre) + (1 - yijDivideMaxR) * math.log(1 - yij_pre)
    
    return -sumRes

#对uid和iid进行重新映射，使之从0开始连续分布
def mapIndex():
    print "start mapIndex"
    maxUid = 0
    maxIid = 0
    uidIndexs = {}
    iidIndexs = {}

    for indexs in trainData.index:
        uid, iid, score, dateTime = trainData.loc[indexs].values[:]
        if not uidIndexs.has_key(uid):
            uidIndexs[uid] = maxUid
            maxUid = maxUid + 1

        if not iidIndexs.has_key(iid):
            iidIndexs[iid] = maxIid
            maxIid = maxIid + 1

    # uidIndexsOut = open(dataDir + trainFileName.split('.')[0]+ '_uidIndexs.pkl', 'wb')
    # cPickle.dump(uidIndexs, uidIndexsOut)

    uidIndexsOut = file(dataDir + trainFileName.split('.')[0]+ '_uidIndexs.csv', 'wb')
    writer = csv.writer(uidIndexsOut)
    for value in uidIndexs.keys():
        writer.writerow((value, uidIndexs[value]))



    # iidIndexsOut = open(dataDir + trainFileName.split('.')[0]+ '_iidIndexs.pkl', 'wb')
    # cPickle.dump(iidIndexs, iidIndexsOut)

    iidIndexsOut = file(dataDir + trainFileName.split('.')[0]+ '_iidIndexs.csv', 'wb')
    writer = csv.writer(iidIndexsOut)
    for value in iidIndexs.keys():
        writer.writerow((value, iidIndexs[value]))
    
    print "mapIndex success"

    return uidIndexs, iidIndexs, maxUid + 1, maxIid + 1

# uidIndexs, iidIndexs, maxUid, maxIid = mapIndex()
uidIndexs = cPickle.load(open(dataDir + trainFileName.split('.')[0]+ '_uidIndexs.pkl', 'r'))
iidIndexs = cPickle.load(open(dataDir + trainFileName.split('.')[0]+ '_iidIndexs.pkl', 'r'))
maxUid = len(uidIndexs)
maxIid = len(iidIndexs)


#创建稀疏矩阵
def createSparseMat(neg_ratio = 5.0):
    print "start createSparseMat"
    time0 = time.time()
    # sparseMat = sparse.dok_matrix((maxUid, maxIid))
    # positiveCount = 0 
    # for indexs in trainData.index:
    #     uid, iid, score, dateTime = trainData.loc[indexs].values[:]
    #     sparseMat[uidIndexs[uid], iidIndexs[iid]] = score
    #     positiveCount = positiveCount + 1

    # print "load trainData success"
    time1 =  time.time()
    # print time1 - time0

    # sparseMatOut = open(dataDir + trainFileName.split('.')[0]+ '_sparseMatp.pkl', 'wb')
    # cPickle.dump(sparseMat, sparseMatOut)

    sparseMat = cPickle.load(open(dataDir + trainFileName.split('.')[0]+ '_trainMat.pkl', 'r'))
    positiveCount = len(sparseMat.keys())
    print positiveCount

    print "creat positive data success"
    
    time1_1 =  time.time()
    print time1_1 - time1

    negativeCount = 0
    while negativeCount/positiveCount < neg_ratio:
        tmpUid = random.randrange(0, maxUid)
        tmpIid = random.randrange(0, maxIid)
        if sparseMat[tmpUid, tmpIid] <= 0:
            sparseMat[tmpUid, tmpIid] = 0.000001
            negativeCount = negativeCount + 1

    print "creat negative data success"
    time2 = time.time()
    print time2 - time1

    sparseMatOut = file(dataDir + trainFileName.split('.')[0]+ '_sparseMat.csv', 'wb')
    writer = csv.writer(sparseMatOut)
    for value in sparseMat.keys():
        writer.writerow((value, sparseMat[value]))

    #采用cPickle耗时长，改为采用csv存储
    # sparseMatOut = open(dataDir + trainFileName.split('.')[0]+ '_sparseMat.pkl', 'wb')
    # cPickle.dump(sparseMat, sparseMatOut)
    print "creat sparseMat success"
    time3 = time.time()
    print time3 - time2
    return sparseMat

if __name__ == '__main__':
    time0 = time.time()
    createSparseMat()
    #mapIndex()
    time1 = time.time()
    print time1 - time0
    pass

