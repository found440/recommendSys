#-*-coding:utf-8-*-
#对数据进行预处理，主要是为相同的UserName对应相同的UserId

import os;
import csv;
import cPickle;
import time;

#记录已存在的UserName
user_dictionary = {};

def addUserIdByName():
    time0 = time.time()
    direction = "../../data/"
    file = open(direction + "meituansub.csv")
    f = open(direction + "meituanWithId.csv", "ab+");
    write = csv.writer(f)
    write.writerow(("userId", "userName",
            "score", "shopStar", "ratingDate"))

    rows = csv.reader(file)
    rows.next()
    userId = 0
    for row in rows:
        userName = row[0]
        #print userName
        if not user_dictionary.has_key(userName) :
            user_dictionary[userName] = userId
            userId = userId + 1
        write.writerow((user_dictionary[userName], 
            str(row[0]), float(row[1]), int(row[2]), int(row[3])))
    f.close();
    time1 = time.time()
    print time1 - time0



if __name__ == "__main__":
    addUserIdByName()
    pass