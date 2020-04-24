# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 18:26:47 2020

@author: verma
"""
from array import*
x=array('i',[])
print('how many elements....??',end=' ')
n=int(input())

for i in range(n):
    print('Enter elements:',end='')
    x.append(int(input()))
print('originat Array:',x)
    
flag=False
for i in range(n-1):
    for j in range(n-1-i):
        if x[j]>x[j+1]:
            t=x[j]
            x[j]=x[j+1]
            x[j+1]=t
            falg=True
    if falg== False:
       break
    else:
      flag=False
print('original sorted array:',x)      
            
            