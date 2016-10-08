# -*- coding: utf-8 -*-

from numpy import *
import math
import matplotlib.pyplot as plt

UNVISITED= False
NOISE =6

def dbscan(dataSet, epsilon, min_points):
    # 将每个样本标记为未访问
    cluster_flag={}
    for point in dataSet:
        cluster_flag[str(point)]=UNVISITED

    cluster_id = 0
    for p in dataSet:
        if cluster_flag[str(p)]==UNVISITED:     #说明该点未被访问
            sphere_points=regionQuery(dataSet,p,epsilon)
            if len(sphere_points)<min_points:
                cluster_flag[str(p)]=NOISE
            else:
                # p是一个核心点
                cluster_id+=1   #创建一个新簇
                expandCluster(dataSet,p,sphere_points,cluster_flag,cluster_id,epsilon,min_points)
    return cluster_flag

def regionQuery(dataSet,p,epsilon):
    # 计算dataSet中每一个点与p的距离,包括p点本身
    sphere_points=[]
    for q in dataSet:
        if math.sqrt(power(mat(p)-mat(q),2).sum())<epsilon:
            sphere_points.append(q)
    return sphere_points

def expandCluster(dataSet,p,sphere_points,cluster_flag,cluster_id,epsilon,min_points):
    cluster_flag[str(p)]=cluster_id
    # 访问p的epsilon领域内的点
    for eps_p in sphere_points:
        # 如何判断一个点是否被访问?
        if cluster_flag[str(eps_p)]==UNVISITED or cluster_flag[str(eps_p)]==NOISE:
            if cluster_flag[str(eps_p)]==UNVISITED:
                eps_p_sphere_points=regionQuery(dataSet,eps_p,epsilon)
                if len(eps_p_sphere_points)>=min_points:
                    sphere_points.append(eps_p)

            cluster_flag[str(eps_p)]=cluster_id

# 如果数据是2维的,可以将聚类结果显示出来
def showCluster(dataSet,cluster_flag):
    mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
    for point in dataSet:
        markIndex=cluster_flag[str(point)]-1
        plt.plot(point[0],point[1], mark[markIndex])

    plt.show()
