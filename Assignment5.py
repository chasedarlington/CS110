# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 14:48:10 2018

@authors: Chase Darlington, Shaneel Ali, Nathan Sandoval, Sydney Guerra"""

###################### Assignment 5 ############################

"""  
Please answer the following questions as a group. Write the group members names on the first 
page. Name the file as (GroupID_Assignment5_BUS205_01). You can provide the answers 
below each question. If the answers are codes, please write then on your coding software then 
copy and paste them. You can also submit a py file if you choose to do so
"""

#Q1
"""
*** USE FOR LOOP
Error detection : Suppose you type a 14-digit credit card number unto a Website, but mistyped one of the digits or inadvertently interchange two adjacent digits.
The website will perform a validation check that always detects the first type of error and nearly always detects the second type of error.
The Validation check is as follows:

	i.) Starting with the leftmost digit, double it and then double every other alternate digit after it.
	However, if any of the doubled digits is a two-digit number, subtract 9 from it. Then sum these new digits. 
    For instance, if the credit card number is 58667936100244, then the digits considered are 5,6,7,3,1,0,4, 
    their new replacements are 1,3,5,6,2,0,8 and the sum of replacements is 25.
    
	ii.) Sum together the remaining seven digits from the credit card number.
	That is, the digits in the odd-numbered positions.
	With the credit card number above, we obtain 8+6+9+6+0+2+4=35.
	
	iii.) Add together the two sums.
	If the result is a multiple of 10, then accept the credit card number.
	Otherwise, reject it. We accept the credit card number above since 25 + 35 = 60, a multiple of 10.
	
	Write a program, that performs data validation on a credit card number.Ex:
	
	Enter a credit card number : 58667936100244
	The number is valid.
"""
def validCC(cc):
    odd=0
    even=0
    for n in range(0,len(cc)):
        if n%2==0:
            x=2*int(cc[n])
            if x>=10:
                x=x-9
                even=even+x
            else:
                odd=odd+1*int(cc[n])
    print(odd)
    print(even)
    if(odd+even)%10==0:
        return True
    return False
cc=str(input("Credit Card Number: "))
if(len(cc)==14 and validCC(cc)):
    print("Valid CC Info")
else:
    print("Invalid CC Info")
# =============================================================================
# Another Way
# =============================================================================
#cc=input("Credit Card Number: ")
#digits=[int(x) for x in str(cc)]
#list1=[]
#repl=[]
#for ch in digits:
#    i=ch*2
#    if i>9:
#        list1.append(ch)
#        repl.append(i-9)
#print(list1)
#print(repl)
#
#
#cc=input("Credit Card Number: ")
#digits=[int(x) for x in str(cc)]
#print(digits)
#n=0
#list1=[]
#repl=[]
#i=digits[n]
#for n in range(0,len(digits)):
#    if n%2==0:
#        list1.append(n)
#        
#
#while(i*2)>9:
#    repl.append((i*2)-9)
#    n+=2
#    i=digits[n]
#print(repl)
#print(sum(repl))
##if n>15:
##    break

         
#Q2
"""
*** USE FOR LOOP
Write a program that prints the first ten triangular numbers. (Do a web search to see what a triangular number is).
header of the function should be :
def print_triangular_numbers(n) :
    ### Write your program indented inside the function name
    ### The output for the first 5 triangular numbers would look like this :
    
	1       1
	2       3
	3       6
	4       10
	5       15
"""
def print_triangular_numbers(n):
    for i in range(1, n + 1):   
        print("n = {0}, triangle = {1}".format(i, (i ** 2 + i)//2))
print_triangular_numbers(10)  
# =============================================================================
# Another Way
# =============================================================================
def print_triangular_numbers(n):
    x=1
    while x<=n:
        formula=x*(x+1)/2
        print(x,formula)
        x+=1
print_triangular_numbers(10)
#Q3
"""
*** USE FOR LOOP
Write a program to return the number of digits of a number. Hint : you have to use a counter for number of digits and 
accumulate the count for all the digits in the number. Make sure that your program handles the number 0 and negative integers.

Ex : It should give the output as 1 for user input 0, it should return 2 for user input 24 and it should return 2 for user 
input -24. (Hint : To handle negative integers check for the abs function which gives the absolute value of any number).
"""
Number = abs(int(input("Input: ")))
Count = 0
while(Number > 0):
    Number = Number // 10
    Count = Count + 1
print("\n Number of digits in the given string = %d" %Count)
# =============================================================================
# Another Way
# =============================================================================
counter=0
num=eval(input("Input: "))
num=abs(num)
num=str(num)
for ch in num:
    counter += 1
print(counter)
#Q4
"""
*** USE FOR LOOP
Write a program that should print a number or a string in reverse order.
 Ex : banana as input should return :  ananab or a digit : 12345 should return 54321.
 (hint : try to typecast a digit into a string so that you can reverse accumulate the number or the digit using the for loop, you can accumulate the string by initializing it as a empty string and then just adding to it,just like we calculate a sum or a count.)
"""
num = int(input("Input: "))
while num > 0:
    num, remainder = divmod(num, 10)
    print (remainder)
# =============================================================================
# Another Way
# =============================================================================
reverseword=''
word=input('Input: ')
for ch in word:
    reverseword=ch+reverseword
print(reverseword)