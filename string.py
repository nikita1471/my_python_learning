# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 19:20:01 2020

@author: verma
"""

str='core python'
n=len(str)
i=0
while i<n:
    print(str[i], end=' ')
    i+=1
print()
i=-1
while i>=-n :
    print(str[i], end=' ')
    i-=1

i=1
while i<=n:
    print(str[-i],end=' ')
    i+=1    
   