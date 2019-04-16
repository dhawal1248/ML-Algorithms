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
    if int(row[2])==1:
        Y.append([1,0])
    else:
        Y.append([0,1])
    
    
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
            if Y[i][1]==1:
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
def train_SLP(eta=0.25):
    ip_no=3
    hd_no=3
    op_no=2
    
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
    c=0
    epoch=0
    
    for i in range(hd_no):
        unj.append(0)
        vnj.append(0)
    for i in range(op_no):
        unk.append(0)
        vnk.append(0)
            
    while epoch<100 and avg_error>0.01:
        error=0
        c=0
        for cur_i in range(N):
            en=0
            unj[0]=1
            vnj[0]=sig(unj[0])
            for j in range(1,hd_no):
                unj[j]=mul(X[cur_i],w1[j])
                vnj[j]=sig(unj[j])
            for k in range(op_no):
                unk[k]=mul(vnj,w2[k])
                vnk[k]=sig(unk[k])
                #rrfprint(k)
                en+=(0.5*((Y[cur_i][k]-vnk[k])**2))
            for k in range(op_no):
                for j in range(hd_no):
                    w2[k][j]+=(eta*(Y[cur_i][k]-vnk[k])*(dif_sig(unk[k]))*vnj[j])
            for j in range(1,hd_no):
                for i in range(ip_no):
                    temp=0
                    for k in range(op_no):
                        temp+=((Y[cur_i][k]-vnk[k])*dif_sig(unk[k])*w2[k][j]*dif_sig(unj[j])*X[cur_i][i])
                    w1[j][i]+=eta*temp
            if en>1:
                print(epoch,cur_i,en)
                c+=1
            error+=en
        avg_error=error/N
        c=c/N
        #print(avg_error)
        epoch+=1    
    #print('Eta : ',eta,'\nDone.Epochs needed : ',epoch)
    return epoch
            

eta_inc=0.1
min_epoch=train_SLP(eta=eta_inc)
optimal_eta=0.1
eta_inc+=0.1
for i in range(10):
    epoch_req=train_SLP(eta=eta_inc)
    if epoch_req<min_epoch:
        min_epoch=epoch_req
        optimal_eta=eta_inc
    eta_inc+=0.1

print('Optimal Eta = ',optimal_eta,'\nEpochs : ',min_epoch)    
