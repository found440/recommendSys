
# -*- coding: utf-8 -*-
#猜你喜欢，http://www.dcjingsai.com/common/cmpt/%E7%8C%9C%E4%BD%A0%E5%96%9C%E6%AC%A2_%E7%AB%9E%E8%B5%9B%E4%BF%A1%E6%81%AF.html

import numpy as np
import pandas as pd
dataDir = '../data/'

trainData = pd.read_csv(dataDir + 'train.csv')
testData = pd.read_csv(dataDir + 'test.csv')
maxUid = trainData['uid'].max()
maxIid = trainData['iid'].max()
#print trainData['uid'].max()
#print trainData['iid'].max()
#print trainData.groupby('uid').count()  #uid数量157949,最大值是223969
#print trainData.groupby('iid').count()  #iid数量14620,最大值是14725

#方法1：平均分
#先计算一次用户及物品的平均分, 最终成绩7.82
def getMean():
    uidMeanData = trainData.groupby('uid').mean().loc[:, ['score']].iloc[:, -1]
    uidMeanData.to_csv("uidMeanData" + '.csv')

    iidMeanData = trainData.groupby('iid').mean().loc[:, ['score']].iloc[:, -1]
    iidMeanData.to_csv("iidMeanData" + '.csv')
    # rateRank = pd.DataFrame(np.int32((rateRank *2).values), index=rateRank.index, columns=['group'])
    # rateRankDes = rateRank.reset_index()

    # trainPlus = pd.merge(trainData, rateRankDes, how='left', on='uid')
    # testPlus = pd.merge(testData, rateRankDes, how='left', on='uid')
    # res = trainPlus.groupby(['iid', 'group']).mean().reset_index().loc[:, ['iid', 'group', 'score']]
    
    # uidMean = trainPlus.groupby(['group']).mean().reset_index().loc[:, ['group', 'score']]
    # uidMean.to_csv("uidMeanData" + '.csv', index=False)
    # iidMean = trainData.groupby('iid').mean().loc[:, ['score']].iloc[:, -1]
    # tmpiidMean = iidMean.reset_index()
    # pd.merge(trainData, tmpiidMean, how='left', on='iid').to_csv("iidMeanData" + '.csv', index=False)
    # #generateRes(res, "meanData")
    # #generateRes(result, "meanResult")
    # return res

def generateRes(result, filename):
    result.loc[:, ['score']].to_csv(filename + '.csv', index=False)

# #方法2：传统的knn方法
# #由于在构建评分矩阵的时候出现了MemoryError，想想也是，223969*14725*32bit/(8*1024*1024*1024) = 12.28GB，Boom
# #考虑到可以使用uid数量157949*14725，相应的完成uid和对应index的映射，消耗内存8.66G,对于8G的电脑还是要跪
# def generateRateMatCsv():
#     rateMat = np.zeros((maxUid+1, maxIid+1))
#     for indexs in trainData.index:
#         (uid, iid, score, time) = trainData.loc[indexs].values[:]
#         rateMat[uid][iid] = score
    
#     np.savetxt('rate_mat.csv', rateMat, delimiter = ',') 


# #传统的协同过滤方法，计算pearson相似度，欧氏距离，余弦相似度等
# def cosine_sim(i, j):
#     a = rate_mat[:, i]
#     b = rate_mat[:, j]
#     m = np.dot(a, b)
#     n = np.sqrt(np.dot(a, a) * np.dot(b, b))
#     return m/float(n)

# def cosine_sim_s(i, j):
#     a = rate_mat[:, i]
#     b = rate_mat[:, j]
#     intersection = a*b
#     if intersection[intersection != 0].size == 0:
#         return 0.0

#     c = a[a!=0] #评价物品i的所有用户评分
#     d = b[b!=0]
#     p = np.mean(c)#物品i的所有用户评分均值
#     q = np.mean(d)

#     m = np.dot(a[intersection!=0]-p, b[intersection!=0]-q)
#     n = np.sqrt(np.dot(c-p, c-p)*np.dot(d-q, d-q))
#     if n==0:
#         return 0.0
#     return m/float(n)

# def pearson():
#     a = rate_mat[:, i]
#     b = rate_mat[:, j]
#     if intersection[intersection != 0].size == 0:
#         return 0.0

#     c = a[intersection!=0] #评价物品i的公共用户评分
#     d = b[intersection!=0]
#     p = np.mean(a[a!=0]) #物品i的所有用户评分均值
#     q = np.mean(b[b!=0])
#     m = np.dot(c-p, d-q)
#     n = np.sqrt(np.dot(c-p, c-p) * np.dot(d-q, d-q))
#     if n==0:
#         return 0.0;
#     return m/float(n)

# def createSimilarityCsv():
#     rate_cos = np.zeros((14620,14620))
#     rate_cos_s = np.zeros((14620,14620))
#     rate_pearson = np.zeros((14620,14620))


#     for i in range(14620):
#         for j in range(14620):
#             if i==j:
#                 rate_cos[i,j]=1
#             elif rate_cos[j,i]!=0:
#                 rate_cos[i,j]=rate_cos[j,i]
#             else:
#                 rate_cos[i,j]=cosine_sim(i,j)

#     for i in range(14620):
#         for j in range(14620):
#             if i==j:
#                 rate_cos_s[i,j]=1
#             elif rate_cos_s[j,i]!=0:
#                 rate_cos_s[i,j]=rate_cos_s[j,i]
#             else:
#                 rate_cos_s[i,j]=cosine_sim_s(i,j)
                
#     for i in range(14620):
#         for j in range(14620):
#             if i==j:
#                 rate_pearson[i,j]=1
#             elif rate_pearson[j,i]!=0:
#                 rate_pearson[i,j]=rate_pearson[j,i]
#             else:
#                 rate_pearson[i,j]=pearson(i,j)

#     iid_index = pd.read_csv('data/rate_mat.csv',index_col=0).columns
#     pd.DataFrame(rate_cos,index=iid_index,columns=iid_index).to_csv('data/rate_cos.csv')
#     pd.DataFrame(rate_cos_s,index=iid_index,columns=iid_index).to_csv('data/rate_cos_s.csv')
#     pd.DataFrame(rate_pearson,index=iid_index,columns=iid_index).to_csv('data/rate_pearson.csv')



# #方法3：SVD方法


if __name__ == '__main__':
    #generateRateMatCsv();
    getMean()
    pass
