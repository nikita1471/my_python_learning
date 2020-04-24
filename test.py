# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 18:59:52 2020

@author: verma
"""

from array import *
x=array('i', [])
print('how many  elements ?',end=' ')
n=int(input())
for i in range(n):
    print('Enter element :', end=' ')
    x.append(int(input))
print('Original array:', x)

flag=false
    