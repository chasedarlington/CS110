#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 09:25:41 2018

@author: muhammadal-abdullah
"""

#Find the value of 1 + 1/2 + 1/3 + 1/4 + ... +1/100 to five decimal places

list1=list()
x=0
while x<100:
    x+=1
    list1.append(1/x)
#print(list1)
sum1=sum(list1)
print(round(sum1,5))


"""
Another way to do it
"""

den=1
sum=0
num=0
while den<=100:
    num=1/den
    sum+=num
    den+=1
print(round(sum,5))
