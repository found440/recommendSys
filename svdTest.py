# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import scipy
from scipy import sparse
from scipy.sparse import sparsetools
from scipy.sparse import linalg as la

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

def sparseMat():
    A = sparse.lil_matrix((10, 5))
    A[2, 3] = 1.0
    A[3, 4] = 2.0
    A[3, 2] = 3.0
    u,sigma,vt = la.svds(A,3)
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

if __name__=='__main__':
    sparseMat()
    #testMat();
