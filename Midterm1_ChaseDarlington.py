# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 13:26:17 2018

@author: Al-Abdullah
"""

#################### MidTerm1 : Total points : 25 #######################

#Please write your solutions in this script, save as Midterm1_Yourname.py and upload it on canvas

#Q1
"""
Write a program that takes the name and height of a person, then prints out the sentence :
    "Name is X feet and Y inches tall." -- 3 points
"""

firstName=str(input("First name: "))
lastName=str(input("Last name: "))
height=float(input("Height (in inches): "))
feet=round(height/12)
inches=height-(feet*12)
print(firstName , lastName , "is" , feet , "feet" , "and" , inches , "inches tall")   

#Q2
"""
Write a program that asks for a user's email and a 4 digit password (ex:anaconda@python.com; 1234),
Then prints the sentence with only the username capatilized (i.e in the above case only
'anaconda' converted to 'Anaconda'), the sentence as " 'username's' pin is 'password' "
ex output : Anaconda's pin is 1234) -- 3 points
"""

email=input("Email: ")
password=input("4 Digit Password: ")
usernameEnd=email.find("@")
print(email.title()[:usernameEnd] + "'s pin is " + password)

#Q3
"""
Write a program that splits the sentence "Good#Luck#Have#a#nice#day"
into a list with individual words, find the length of the list, index of the element 'day' in the list
and then create a sentence "Have a nice day, Good Luck" -- 4 points
"""
text="Good Luck Have a nice day"
words=list(text.split())
print("length of list: " , len(words))
indDay=words.index("day")
print("index of the element 'day' in the list: " , indDay)
indHave=words.index("Have")
print(' '.join(words[indHave:]), ',' , ' '.join(words[:indHave]))

#Q4
"""
Write a program that registers 3 salary amounts into a list, Find the 
minimum salary, maximum salary, and average salary of the employees in the list and remove the smallest amount from the list -- 4 points
"""

salaries=list()
salary1=int(input("Salary 1: "))
salary2=int(input("Salary 2: "))
salary3=int(input("Salary 3: "))
salaries.append(salary1)
salaries.append(salary2)
salaries.append(salary3)
print("Minimum Salary:" , min(salaries))
print("Maximum Salary:" , max(salaries))
print("Average Salary:" , sum(salaries)/len(salaries))
salaries.remove(min(salaries))
print("Revised List:" , salaries)

#Q5
"""
What is the outputs for the following cases : Boolean(True or False) :
    a.) "Car" < "Train" and "Bus" > "Flight" -- 1 point
    b.) Given x = 3, y = 4. not(x<y) or not(x < (x +y)) and (x**y > y**x) -- 1 point
"""
print("Car"<"Train")
print("Bus">"Flight")

x=3
y=4
print(not(x<y))
print(not(x<(x+y)))
print(x**y>y**x)


#Q6 
"""
Write a program that takes two input values (x and y), compares them and if x>y prints 
"x is greater", "y is greater" if y > , or "Both x and y are equal" if they are equal-- 4 points
"""
x=input("x: ")
y=input("y: ")
if x>y:
    print("x is greater")
elif x<y:
    print("y is greater")
else:
    print("Both x and y are equal")

#Q7
"""
Write a program to find the amount earned by a youtuber who is paid 1$ per view when the views are less than 1000,
2$ per view when the views are more than 1000 but less than 10000 and an additional 1$ per view when the views
are greater than 10000 ($3). Make sure you test your code with views less than 1000, between 1000 and 10000 and greater
than 10000. -- 5 points
""" 
views=int(input("Views: "))
payment=0
if views<0:
    payment="invalid entry"
elif views<1000:
    payment=views*1
elif views<10000:
    payment=views*2
elif views>10000:
    payment=views*3
else:
    payment="error"
print('$',payment)
