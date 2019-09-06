# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 01:37:16 2018

@author: muhammadal-abdullah
"""

####################Quiz3#######################

#Please write your solutions in this script, save as yourname_quiz3_sol.py and upload it on canvas

#Q1 
""" 
Write a program that calculates the tax to be paid by each employee per their income.
If the income is less than 30000, the tax will be zero and if it the income is greater than 30000
the tax will be 30% of the income.
The program should write "based on your income, the tax to be paid is: ....."
"""

#income=eval(input("Income: "))
#if income<30000:
#    tax=0
#    print('Tax: ' + str(tax))
#else: 
#    tax=0.3*income
#    print('Tax: ' + str(tax))
    

#Q2
"""
Write a program that asks employees about their employee ID and prints thier names accordingly as "Employee ID is for: ..... ".
Hint: you can have the names and the IDs in a nested list. e.g.[["James Maxwell",1],["Richard Feynman",2]]


"""
#ID=eval(input('Employee ID: '))
#empList=[['Charles Montgomery', 1]['Richard Weasel', 2]['Gregory Martin', 3]['Chase Darlington', 4]['Will Sherwood', 5]['Bill Clinton', 6]['Ben Williams', 7]['Francis Drake', 8]]
#print(empList[empList.index(ID)][1])

#employee_id=[("John",1),("Mary",2),("Joe",3)]
#employee_fullnames=["John Smith","Mary Doe","Joe Carter"]
#id=[1,2,3]
#sampleid=eval(input('id: '))
#person1=(employee_fullnames[0][0:],id[sampleid+1])
#print(person1)

#Q3
"""
Write a program that asks the user for a number and checks if the number is divisble by both 3 and 5.
according, the program should type "The number is divisible by 3 and 5" in case it is divisible by both 3 and 5,
OR "the number is not divisibleby both 3 and 5" in case is it not.
"""

#num=int(input('Input a number: '))
#if num%3==0:
#    if num%5==0:
#        print("the number is divisible by both 3 and 5")
#    else:
#        print("the number is not divisible by both 3 and 5")
#else:
#    print("the number is not divisible by both 3 and 5")