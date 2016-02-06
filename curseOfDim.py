# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 13:01:35 2016

@author: Sameer
@title: Understanding curse of dimensionality
""" 
import numpy as ny
import matplotlib.pyplot as plt
import math as mth
from datetime import datetime

from sympy.utilities.decorator import no_attrs_in_subclass

print "Calculation Started:"
print str(datetime.now())
datestarted=datetime.now()
n=1000
k=range(1,101)


def getSqrdVal(i,j,dp,dimension):
    sum=0
    for dim in range(0,dimension):
        sum=sum+mth.pow(dp[i][dim]-dp[j][dim],2)
    return(mth.sqrt(sum))

def calcDiff(dim,dp):
    diffrow=[]
    diff=[]
    for i in range(0,n):
        sum=0
        for j in range(0,n):
            sum=getSqrdVal(i,j,dp,dim)
            diffrow.insert(j,sum)
        diff.insert(i,diffrow)        
        diffrow=[]
    return diff
            
def plotGraph(minmax):
    print "Plotting the Graph"
    print str(datetime.now())
    plt.plot([item[0] for item in minmax],[item[3] for item in minmax])
    plt.title('Understanding the curse of dimensionality for n=10000')
    plt.xlabel('Value of k')
    plt.ylabel('r(k)')
    plt.show()
    return

#main thread
minmax=[]
for dim in k:
    dp=[]
    noOfRuns=10 #avg for 10 runs
    nOfI=[]
    maxval=0
    minval=0
    rk=0.0
    print "DataPoints created for k={}".format(dim)
    for i in range(0,noOfRuns):
        dp=ny.random.random((n,dim))
        diff=calcDiff(dim,dp)
        diff=ny.asarray(diff)
        diff=diff.flatten()
        diff=ny.sort(diff)
        #structure of min max
        maxval=diff[len(diff)-1]
        minval=diff[n]
        rk=mth.log10((maxval-minval)/minval)
        nOfI.insert(i,rk)
        rk=ny.mean(nOfI)
    minmax.insert(dim,[dim,maxval,minval,rk])
    print "calculated r(k) for k={}".format(dim)
plotGraph(minmax)
print "Calculation Finished:"
print str(datetime.now())

