# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 23:18:28 2020

@author: verma
"""


f1 = open('merge_file_1.txt')
#print(f1.readlines())

f2 = open('merge_file_2.txt')
#print(f2.readlines())


f3 = open('merged.txt', 'wb')
#f3.writelines([bytearray(l) for l in f1.readlines()])
#f3.writelines([bytearray(l) for l in f2.readlines()])

f3.write(bytes(bytearray(f1.readlines())))
f3.write(bytes(bytearray(f2.readlines())))

f3.close()
f1.close()
f2.close()
