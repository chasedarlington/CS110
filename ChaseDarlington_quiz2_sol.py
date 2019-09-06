# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 22:38:57 2018

@author: Al-Abdullah
"""

####################Quiz2#######################

#Please write your solutions in this script, save as yourname_quiz2_sol.py 

#Q1
""" Write a program that requests the two-part name and location of a person then splits the name into
firstname and lastname and displays the output as a sentence : "firstname" lives in "location"
"""

name=str(input('Your name: '))
x=name.find(' ')
print('First name: ' + name[:x])
print('Last name:' + name[x:])
print(name[:x] + ' lives in' + name[x:])

#Q2
""" a.) Identify the errors in the codes below:
    
    names=["Alice","James","Joe"]
    print(names[3])"""
    
#index out of range
#[3] indicates the '4th' name in the list. There is no fourth name
#if the code were trying to determine the third name, the index number should be [2]
    
    
"""b.) Write a code to find the index value of the above list:names for the entry "James" and print
    the length of the entry "Joe" 
"""
#names=["Alice","James","Joe"]   
#print("index value for James: " + str(names.index("James")))
#indJoe=names.index("Joe")
#print(names[indJoe])

#Q3
"""Write a program that calculates how much to tip the server in a restaurant. 
The tip should be 15% of the check, or a minimum of $2, whichever is greater."""

#check=float(input('Bill/Check Total: '))
#stdTip=0.15*check
#minTip=2.00
#if stdTip < minTip:
#    print('Recommended Tip: ' + str(minTip))
#else:
#    print('Recommended Tip: ' + str(stdTip))


