# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 18:20:31 2019

@author: Dhawal
"""

import csv
import math
import random
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np

def mul(X,Y):
    n=len(X)
    res=0
    for i in range(n):
        res+=X[i]*Y[i]
    return res

def sig(x):
    return (1/(1+math.exp(-x)))

def dif_sig(x):
    return sig(x)*(1-sig(x))    
        

f=open('SingleNN.csv','r')
X=[]
X1=[]
X2=[]
Y=[]
reader=csv.reader(f)
for row in reader:
    X.append([1,float(row[0]),float(row[1])])
    X1.append(float(row[0]))
    X2.append(float(row[1]))
    Y.append([float(row[2])])
    
#fixing X,making space for line
from random import random     

#removes all points near line,at distance less than remove_distance

remove_distance=0.5
c=1
while c!=0:
    c=0    
    temp1=[]
    temp2=[]
    for i in range(len(X)):
        point=X[i]
        if abs(point[2]-1.5*point[1]+0.5)<remove_distance:
            c=1
            temp1.append(point[1])
            temp2.append(point[2])
            if Y[i][0]==-1:
                X[i]=[1,point[1]+0.25,point[2]-0.25]
                X1[i]=point[1]+0.25
                X2[i]=point[2]-0.25
            else:
                X[i]=[1,point[1]-0.25,point[2]+0.25]
                X1[i]=point[1]-0.25
                X2[i]=point[2]+0.25

#visualizing the data +1 class members shown by 'x' and -1 by 'o'
                
                
for i in range(len(Y)):
    if Y[i][0]==1:
        plt.scatter(X1[i],X2[i],marker="x")
    else:
        plt.scatter(X1[i],X2[i],marker="o")
xx = np.linspace(2,8,2)
yy = 1.5*xx-0.5
plt.plot(xx, yy, '-r')

#SLP

ip_no=3
hd_no=3
op_no=1

w1=[]
for i in range(hd_no):
    temp=[]
    for j in range(ip_no):
        if i==0:
            temp.append(0)
        else:
            temp.append(random())
    w1.append(temp)

w2=[]
for i in range(op_no):
    temp=[]
    for j in range(hd_no):
        temp.append(random())
    w2.append(temp)

N=len(X)
unj=[]
vnj=[]
unk=[]
vnk=[]
error=0
avg_error=1
en=0
eta=0.1
epoch=10

for i in range(hd_no):
    unj.append(0)
    vnj.append(0)
for i in range(op_no):
    unk.append(0)
    vnk.append(0)
 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       