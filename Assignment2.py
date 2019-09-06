# -*- coding: utf-8 -*-
"""
Created on Tue Apr 3 9:06:05 2018

@author: Al-Abdullah
"""

###################### Assignment 2 ############################

#Please answer the following questions as a group. Write the group members names on the first 
#page. Name the file as (GroupID_Assignment2_BUS205_1). 
#Q1

#"""Write a program to calculate the minimum, maximum and average value of the list of numbers [1,5,10,0,7]"""

#somelist = [1,5,10,0,7]
#max_value = max(somelist)
#min_value = min(somelist)
#avg_value = sum(somelist)/len(somelist)
#print ("Maximum:",max_value)
#print ("Minimum:", min_value)
#print ("Average Value:", avg_value)

#Q2

#"""Write a program to split the sentence 'Have a great day BUS205' into a list of strings 
#and join only the first 4 strings into a sentence again""" 

#sentence="Have a great day BUS205"
#select=(sentence.split())
#print(select[0:3])
#print(select.join(reduce a, b:a+b,1))

#Q3

#""" Write a program to calculate the number of occurences of the letter 'a' from the word banana into 
#a list of letters and also calculate the index of the first occurence of the letter 'a' """

#word = 'banana'
#print ("instances of 'a': " + str(word.count('a')))
#print ("first instance of 'a' (index number): " + str(word.find('a')))


#Q4

#"""Given a nested list with state and capitals, states_capitals=[["California",Sacramento],["Oregon","Salem"],["Washington","Olympia"]]. 
#Write a program to print an output "The capitals of some of the westerns states in US like California,Oregon,Washington are Sacramento,Salem,Olympia""""

#states_capitals=[["California","Sacramento"],["Oregon","Salem"],["Washington","Olympia"]]
#print(states_capitals[0][1],states_capitals[1][1],states_capitals[2][1])

#Q5

#"""Given two lists,one with Customerfullnames=["John Smith","Mary Doe","Joe Carter"] and their 
#Balances=[25000,45000,55000]. Write a program to extract the customer firstnames and their 
#balances and make a nested list of tuples as below:
#customer_balance=[("John",25000),("Mary",45000),("Joe",55000)]"""

nameList=["John Smith","Mary Doe","Joe Carter"]
balances=[25000,45000,55000]
#=customerNames.count(customerNames[][1])
firstNames=customerNames[0][0], customerNames[1][0],customerNames[2][0]
print(firstNames)
