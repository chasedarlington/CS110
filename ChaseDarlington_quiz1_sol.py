#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  29 09:44:46 2018

@author: muhammadal-abdullah
"""

####################Quiz1#######################

#Please write your solutions in this script, save as yourname_quiz1_sol.py and upload it on canvas

print("Q1")

# =============================================================================
# """ 
# Please indicate the errors(syntax,runtime or logic) in the code below, and rewrite the code in the right way.ex : # 3 = x # initial variable name should be to the left of the assignment statement
#        x = 3 # rewritten code
# """
# 
# Price = 100
# price = Price
# print(pRice)
# 
# sale = 150
# cost = 100
# profit_fraction = sale - cost/100
# 
# The error is Syntax
# 
# =============================================================================
#print("syntax error")
#
#price = 100
#print(price)
#
#sale=150
#cost=100
#profit_fraction=(sale-cost)/100
#print(profit_fraction)


#Q2

""" 
A fast food restaurent does 10 transactions/minute (tpm), write a program that calculates the number of transactions
per day (numTrans),given that the restaurent works 15 hours/day (ohpd) and also 5 days/week (dpw). 
"""

#tpm=10
#ohpd=15
#dpw=5
#numTrans=tpm*60*ohpd
#print(numTrans)


"""
check
"""
#print(10*60*15)




#Q3

""" 
Write a program that takes a user input as a string, prints the length of the string, and shows the string in UPPERCASE
"""
#s = (str(input("Input information here: ")))
#print(s.upper())

#Q4

"""
Write a program that asks the user about the name of the class, name of the professor, the number of students present, the 
number of students absent, and then displays the the class name, the professor name, and the percentage of
the students who attended the class. Round the percent to one decimal place
"""

#className=str(input('Name of class: '))
#professorName=str(input('Name of professor: '))
#present=int(input('Number of students present: '))
#absent=int(input('Number of students absent: '))
#percentPresent=present/(absent+present)
#print(className)
#print(professorName)
#print(round(percentPresent,1))


#Q5

"""
Write a program with the sentence "Hello BUS205" as input,split the sentence into two seperate
words "Hello" and "BUS205" a tab space of 10 spaces. The program also should print each word in a single line.
As shown in the lines below:
    Hello         BUS205
    Hello
    BUS205
"""

intro='Hello\tBUS205'
print(intro)
#spc = intro.find(' ')
#print(spc)
#x = intro[:spc]
#y = intro[spc:]
#print(x+'\t\t'+y)
print(intro.expandtabs(10))

#intro.insert(6 , '         ')
#
#print(intro)
#print(intro[0:4])
#print(intro[6:])
