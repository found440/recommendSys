#-*-coding:utf-8-*-
#对数据进行预处理，主要是为相同的UserName对应相同的UserId

import os;
import csv;
import cPickle;
import time;

fromFile = "ml_1m_ratings.csv"
toFile = "ml_1m_ratings_proprecess.csv"

#记录已存在的UserName
user_dictionary = {}
item_dictionary = {}

def addUserIdByName():
    time0 = time.time()
    direction = "../../data/"
    file = open(direction + fromFile)
    f = open(direction + toFile, "ab+")
    write = csv.writer(f)
    # write.writerow(("userId", "userName",
    #         "score", "shopStar", "ratingDate"))

    rows = csv.reader(file)
    rows.next()
    userId = 0
    itemId = 0
    for row in rows:
        userName = row[0]
        itemName = row[1]
        # itemName = row[2]
        print userName
        if not user_dictionary.has_key(userName) :
            user_dictionary[userName] = userId
            userId = userId + 1
        if not item_dictionary.has_key(itemName) :
            item_dictionary[itemName] = itemId
            itemId = itemId + 1

        write.writerow((user_dictionary[userName], 
            item_dictionary[itemName], float(row[2]), int(row[3])))
        
        # write.writerow((user_dictionary[userName], 
        #     item_dictionary[itemName], float(row[1]), int(row[3])))
    f.close();
    time1 = time.time()
    print time1 - time0



if __name__ == "__main__":
    addUserIdByName()
    pass