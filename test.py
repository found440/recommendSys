# -*- coding: utf-8 -*-
#猜你喜欢，http://www.dcjingsai.com/common/cmpt/%E7%8C%9C%E4%BD%A0%E5%96%9C%E6%AC%A2_%E7%AB%9E%E8%B5%9B%E4%BF%A1%E6%81%AF.html

import numpy as np
import pandas as pd

trainData = pd.read_csv('../data/train.csv')
testData = pd.read_csv('../data/test.csv')
maxUid = trainData['uid'].max()
maxIid = trainData['iid'].max()
#print trainData['uid'].max()
#print trainData['iid'].max()
#print trainData.groupby('uid').count()  #uid数量157949,最大值是223969
#print trainData.groupby('iid').count()  #iid数量14620,最大值是14725

#方法1：平均分
#先计算一次用户及物品的平均分, 最终成绩7.82
def getMean():
    rateRank = trainData.groupby('uid').mean().loc[:, ['score']].iloc[:, -1]
    rateRank = pd.DataFrame(np.int32((rateRank *2).values), index=rateRank.index, columns=['group'])
    rateRankDes = rateRank.reset_index()

    trainPlus = pd.merge(trainData, rateRankDes, how='left', on='uid')
    testPlus = pd.merge(testData, rateRankDes, how='left', on='uid')
    res = trainPlus.groupby(['iid', 'group']).mean().reset_index().loc[:, ['iid', 'group', 'score']]
    result = pd.merge(testPlus, res, how='left', on=['iid', 'group']).fillna(3.0)
    #generateRes(result, meanResult)
    return res

def generateRes(result, filename):
    result.loc[:, ['score']].to_csv(filename + '.csv', index=False)

#由于在构建评分矩阵的时候出现了MemoryError，想想也是，223969*14725*32bit/(8*1024*1024*1024) = 12.28GB，Boom
def generateRateMatCsv():
    rateMat = np.zeros((maxUid+1, maxIid+1))
    for (uid, iid, score, time) in trainData:
        rateMat[uid, iid] = score
    np.savetxt('rate_mat.csv', rateMat, delimiter = ',') 



#传统的协同过滤方法，计算pearson相似度，欧氏距离，余弦相似度等
def pearson():
    pass

if __name__ == '__main__':
    #generateRateMatCsv();
    #getMean()
    pass