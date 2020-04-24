# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 18:47:24 2020

@author: verma
"""
from numpy import*
a=array([1,2,3,4,5,6,7,8,9,10])
b=reshape(a,(2,5))
print(b)

#a=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(b)):
    print(b[i])


for i in range(len(b)):
    for j in range(len(b[i])):
        print(b[i][j], end=' ')