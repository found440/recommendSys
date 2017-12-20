# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import scipy
from scipy import sparse
from scipy.sparse import sparsetools
from scipy.sparse import linalg as la
import time

dataDir = '../data/'
trainData = pd.read_csv(dataDir + 'train.csv')
testData = pd.read_csv(dataDir + 'test.csv')
maxUid = trainData['uid'].max() + 1
maxIid = trainData['iid'].max() + 1

def testMat():
    S = np.zeros([5,6])
    A=[[1,1,1,0,0],  
             [2,2,2,0,0],  
             [3,3,3,0,0],  
             [5,5,3,2,2],  
             [0,0,0,3,3],  
             [0,0,0,6,6]] 
    u,sigma,vt = la.svd(A)
    print"-------------"
    print(A)
    print"-------------"
    print(u)
    print"-------------"
    print(sigma)
    print"-------------"
    print(vt)
    print"-------------"
    i=0
    while i < A.shape[0]:
        tmp = 0;
        j=0
        while j < A.shape[1]:
            k=0
            tmp = 0;
            while k < len(sigma):
                tmp = tmp + u[i][k]*sigma[k]*vt[k][j]
                k = k+1
            j = j + 1
            print tmp," ",
        print ""
        i=i+1

def getMatValueByIndex(u, sigma, vt, i, j):
    k=0
    tmp = 0;
    while k < len(sigma):
        tmp = tmp + u[i][k]*sigma[k]*vt[k][j]
        k = k+1
    return tmp

#针对稀疏矩阵的建立和奇异值分解
def sparseMat():
    A = sparse.lil_matrix((maxUid, maxIid))
    for indexs in trainData.index:
        uid, iid, score, time = trainData.loc[indexs].values[:]
        A[uid, iid] = score
    u,sigma,vt = la.svds(A,50)
    # print"-------------"
    # print(A)
    print"-------------"
    print(u)
    print"-------------"
    print(sigma)
    print"-------------"
    print(vt)
    print"-------------"
    
    np.savetxt('u_50.csv', u, delimiter = ',') 
    np.savetxt('sigma_50.csv', sigma, delimiter = ',') 
    np.savetxt('vt_50.csv', vt, delimiter = ',') 
    
    # 计算对应原网络中的index为i,j位置的值
    # i=0
    # while i < A.shape[0]:
    #     tmp = 0;
    #     j=0
    #     while j < A.shape[1]:
    #         k=0
    #         tmp = 0;
    #         while k < len(sigma):
    #             tmp = tmp + u[i][k]*sigma[k]*vt[k][j]
    #             k = k+1
    #         j = j + 1
    #         print tmp," ",
    #     print ""
    #     i=i+1

if __name__=='__main__':
    time0 = time.time()
    sparseMat()
    time1 = time.time()
    print time1 - time0
    #testMat();
