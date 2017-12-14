# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

trainData = pd.read_csv('../data/train.csv')
testData = pd.read_csv('../data/test.csv')

#先计算一次用户及物品的平均分
def getMean():
    rateRank = trainData.groupby('uid').mean().loc[:, ['score']].iloc[:, -1]
    rateRank = pd.DataFrame(np.int32((rateRank *2).values), index=rateRank.index, columns=['group'])
    rateRankDes = rateRank.reset_index()

    trainPlus = pd.merge(trainData, rateRankDes, how='left', on='uid')
    testPlus = pd.merge(testData, rateRankDes, how='left', on='uid')
    res = trainPlus.groupby(['iid', 'group']).mean().reset_index().loc[:, ['iid', 'group', 'score']]
    result = pd.merge(testPlus, res, how='left', on=['iid', 'group']).fillna(3.0)
    #result.loc[:, ['uid', 'iid', 'score']].to_csv('meanResult.csv', index=False)
    return res

#传统的协同过滤方法，计算pearson相似度，欧氏距离，余弦相似度等
def pearson():
    

if __name__ == '__main__':
    getMean()