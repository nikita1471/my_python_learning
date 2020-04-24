# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 14:15:28 2020

@author: verma
"""

#name='nikita'
#print('hi %20s' % name)
#ch=input("enter a char: ")
#print("U entered :" +ch[0])
#str=input("Enter a number: ")
#x=int(str)
#print("U entered: ",x)
#x=int(input("enter first number : " ))
#y=int(input("enter second number : " ))
##print("sum of {} and {} is {}".format(x , y ,x+y))
#print("sum of {0} and {1} is {2}".format(x,y, x+y))
#print("produnct of {0} and {1} is {2}".format(x,y, x*y))


#import math
#r=float(input("enter radius : "))
#area = math.pi*r**2
#print("area of the circle=",area) 
#print("area of the circle= {:.2f}".format(area)) 
#print("area of the circle= %.2f " %(area)) 
##num=1
##if num==1:
##    print("one")
#str="yes"
#if str=='yes':
#    print("yes this is correct")        
#x=100
#while x>=100 and x<=200:
#    print(x)
#    x+=2


#m,n =[int(i) for i in  input("enter the maximumm and minimum range :").split(',')]

#x=m
#if x%2 !=0:
#    x=x+1
#
#while x>=m and x<=n:
#    print(x)
#    x+=2




#str='nikita saket'
#n=len(str)
#for i in range(n):
#    print(str[i])

#
#for i in range(1,11):
#    for j in range(1,i+1):
#        print('*',end ="")
#    print()        
#
## 
##
#for i in range(1,11):
#    print('*'*(i))  
#
#     
#n=40
#for i in range(1,11):
#    print(' ' *n, end='')
#    print('* '*(i))
#    n-=1

#n=20
#for i in range(1,11):
#    print(' ' *(n-i) + '* '*(i)) 




#for x in range(1,11):
#    for y in range(1,11):
#        print('{:8}'.format(x*y), end='')
#        
#    print()    

#
#grp1=[1,2,3,4,5,6]
#search= int(input("enter the element :"))
#for element in grp1:
#    if search == element :
#        print('search is found in grp1')
#        break
#else:
#    print('element not found in grp1')    

#
#num=[1,2,3,4,5,-6,-7,-8,-9]
#for i in num:
#    #    if (i<0):
#    #        print(i)
#    if(i>0):
#        pass
#    
#    else:
#        print(i)        


#x=int(input('enter num greater than 5: '))
#assert x>5,"wrong input entered"
#print('u entered',x)

#x=int(input('enter num greater than 5: '))
#try:
#    assert (x>5)
#    print('u entered',x)
#except AssertionError :
#        print("wrong input entered")
#        
#def sum(a,b):
#    print('sum =',a+b)
#sum(10,20)
#sum(3,2)    


#max =int(input('upto what number'))
#for num in range(2, max+1):
#    for i in range(2,num):
#        if (num % i)==0:
#            break
#    else :
#        print(num)


#import array
#a= array.array('i',[5,6,2,1])
#print('The array elements are :')
#for element in a:
#    print(element)


#from array import *
#r = array('u',['a','b','c','d'])
#print('The array elements are :')
#for element in r:
#    print(element)
# 

#from array import *
#a1= array('f',[  5.5 , 1.5, 7, 6])
#
#a2= array(a1.typecode,(a*2 for a in a1))
#print('The array elements are :')
#for element in a2:
#    print(element)



#from array import *
#x= array('i',[10,20,30,40,50,60])
#n=len(x)
#for i in range(n):
#    print(x[i],end =" ")

#from array import *
#x= array('i',[10,20,30,40,50,60])
#n=len(x)
#i=0
#while i<n:
#    print(x[i],end =" ")
#    i+=1



#from array import *
#x= array('i',[10,20,30,40,50,60])
#y=x[-4:-1]
#print(y)
#x[1:3]= array('i',[2,3])
#print(x)
#


from array import *
a=array('i',[90,80,70,60])
#x= array('i',[10,20,30,40,50,60])
##x= array('i',[100])
#
##a.append(80)
##a.count(40)
##print(a.count(40))
#a.extend(x)
#
#print(a)


#a.insert(2,100)
#print(a)

#n=a.index(70)
#print(n)

#lst=a.tolist()
#print(lst)
#print(a)



#marks=int(input('enter marks :'))
str =input('enter marks :').split(' ')

marks=[int(num) for num in str]
sum=0
for x in marks:
    print(x)
    sum+=x
n=len(marks)
percent=sum/n 
print(percent)   




















































