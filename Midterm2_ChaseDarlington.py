# -*- coding: utf-8 -*-
"""
Created on Tue May 1 09:00:17 2018

@author: Al-Abdullah
"""

###################### Midterm 2 : Total points : 25 : Good Luck ############################

#Please write your solutions in this script, save as Midterm2_Yourname.py and upload it on canvas

#Q1 - 6 points
"""
 Write a program to take input numbers (positive integer) and find the sum of squares of each digit in the number and print the sum.
 Hint : Use int conversion to do numeric operations
"""

inp=input("please enter a number : ")

total = 0
for i in inp :
    i = int(i)**2
    total+=i
print(total)

#list1=[1,2,3,4,5,6,0,-2]
#list2=[]
#for x in list1:
#    value=int(x)
#    if value==x and x>0:
#        x=x**2
#        list2.append(x)
#print(list2)
#sum(list2)

#Q2 - 6 points
"""
Write a program that adds only the prime numbers between 1 to 1000.
Hint : A number is prime if its divisible by 1 and the number is itself
"""
list1=[]
for num in range(1,1000):
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if prime:
       list1.append(num)
print(list1)
sum(list1)

#def prime(num):
#    z=0
#    a=2
#    while num > a :
#      if num%a==0 & a!=num:
#        z=int(0)
#        a=a+1
#      else:
#        z=int(1)
#        a=(num)+1
#    return z
##list1=[range(1,1000)]
#list1=[1,2,3,4,5,6,7,7,8,10]
#
#prime_list=[]
#for x in list1:
#    if prime(x)>0:
#        prime_list.append(x)
##    if prime(x)==1:
##        prime_list.append(x)
#print(prime_list)
#    
###list1=[range(1,1000)]
##list1=[1,2,3,4,5,6,7,7,8,10]
##list2=[]
##list3=[]
###prime_list=[]
##for num in list1:
##    if num > 1:
##        for i in range(2,num):
##            if (num % i) == 0:
##                list3.append(num)
##            else:
##                list2.append(num)
##    else:
##       list3.append(num)
##print(list2)
##print(list3)
##    
##
##num = 407
##
### take input from the user
### num = int(input("Enter a number: "))
##
### prime numbers are greater than 1
##if num > 1:
##   # check for factors
##   for i in range(2,num):
##       if (num % i) == 0:
##           print(num,"is not a prime number")
##           print(i,"times",num//i,"is",num)
##           break
##   else:
##       print(num,"is a prime number")
##       
### if input number is less than
### or equal to 1, it is not prime
##else:
##   print(num,"is not a prime number")
#   
#   
#Q3 - 7 points
"""
 Write a function to return the number of even digits of a number and the number of odd digits as a list.
 Hint : you have to use a counter for number of even digits and odd digit, accumulate the count for both the even and odd digits in the number.
 Make sure that your program handles the number 0 and negative integers. Use for loop.

Func def : def even_odd(inp_number):
              your code
	    return list_no_even_odd ( returns a list of number of even and odd numbers in the input number)

Ex : It should give the output as [1,0] for user input 0, it should print [1,1] for user input 25 and 
it should print [2,2] for user input -2547. (Hint : To handle negative integers check for the abs function which gives the absolute value of any number). Work with the int and str conversions of the number.
"""
# =============================================================================
# Example 1
# =============================================================================
def even_odd(inp_number):
    count_even=0
    count_odd=0
    list1=[int(x) for x in str(abs(inp_number))]
    for x in list1:
        if x%2==0:
            count_even+=1
        else:
            count_odd+=1
    list_no_even_odd=[count_even, count_odd]
    return list_no_even_odd

even_odd(0)
# =============================================================================
# Example 2
# =============================================================================
def even_odd(inp_number):
    count_even=0
    count_odd=0
    list1=[int(x) for x in str(abs(inp_number))]
    for x in list1:
        if x%2==0:
            count_even+=1
        else:
            count_odd+=1
    list_no_even_odd=[count_even, count_odd]
    return list_no_even_odd

even_odd(25)
# =============================================================================
# Example 3
# =============================================================================
def even_odd(inp_number):
    count_even=0
    count_odd=0
    list1=[int(x) for x in str(abs(inp_number))]
    for x in list1:
        if x%2==0:
            count_even+=1
        else:
            count_odd+=1
    list_no_even_odd=[count_even, count_odd]
    return list_no_even_odd

even_odd(-2547)
# return two items, the number of odd and the number of even


#Q4 - 6 points
"""
 Write a function to calculate the minimum payment for credit card statement.The 
 minimum payment amount to be done is entire balance if the balance is $20 or less, or else the minimum 
 payment is 20$ plus 10% of the balance amount which is above 20$. The function should return the 
 minimum transaction amount to be done for any input balance amount by the user.

Func def : def min_payment(balance):
				your code to calculate min payment amount
				return min_payment
 
Ex: call to the function print(min_payment(50)) should return 25$, here 50 is the balance in the account.
"""
# =============================================================================
# Example 1
# =============================================================================
def min_pmt(balance):
    if balance<=20:
        minpmt=balance
    elif balance>20:
        minpmt=20+0.1*balance
    else:
        print("Invalid Balance")
    return(minpmt)

balance1=1000
min_pmt(balance1)

# =============================================================================
# Example 2
# =============================================================================
def min_pmt(balance):
    if balance<=20:
        x=balance
    else:
        x=20+0.1*balance
    return(x)

balance1=50
min_pmt(balance1)

#Q5 - 5 points (Extra credit)
"""
Given a file bus205.txt with the information about a certain organization with the employee salaries in each line, calculate the tax each employee pays ( 30% of the salary). 
Read the file with the salary information line by line into a variable and write the salary information into a new file bus205_modified.txt where the tax amounts 
calculated were 30000 and above.

Ex: Assume bus205.txt has 2 lines :

80000
120000

The tax amount(30%) for 80000 is 24000 and for 120000 it is 36000, thus you only write the salary amount 120000 into the new file bus205_modified.txt

The contents of the newfile bus205_modified.txt would look like :

120000

Submit your bus205_modified.txt along with the midterm2.py file.
"""
 fileTest=open('205.txt', 'w+') #w+ means to write into a file
for i in range(10):
    fileTest.write('This is line %d\n' %(i+1))
fileTest.close

fileTest2=open('205.txt', 'r')
if fileTest2.mode == 'r' :
#this is optional and it just tests if the file is open for reading info from it 
    readFromFile=fileTest2.read() #read function puts all data in the file into th evariable
print(readFromFile)
fileTest2.close

m=open('205.txt', 'r') # r means to read file
x=m.readlines() #reads information line by line
for i in x:
    print(i)
m.close()

fileAppend=open('bus205.txt', 'a+') #a+ means to make a new file if it isnt already there
for i in range(4):
    fileAppend.write('This line is %d appended\n' %(i+1))
fileAppend.close


fileAppend=open('bus205.txt', 'r')
x=fileAppend.read()
print(x)
fileAppend.close()
