#coding=utf-8
from numpy import *

import dbscan

if __name__=='__main__':
    print 'step1:load data'
    dataSet = []
    fileIn = open('testSet.txt')
    for line in fileIn:
        lineArr = line.strip().split('\t')
        dataSet.append([float(lineArr[0]), float(lineArr[1])])
    # dataSet中的每一个元素表示一个点[-2.651229, -3.103198]

    print "step2:clustering..."
    epsilon=3
    min_points=2
    cluster=dbscan.dbscan(dataSet,epsilon,min_points)
    for key in cluster:
        print key,cluster[key]

    dbscan.showCluster(dataSet,cluster)