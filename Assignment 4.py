# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 22:44:40 2018

@author: Chase Darlington
"""

#Q1
"""
Determine whether the condition evaluates to True or False :
    a.) 2 ** (5-2) > 7
    b.) (2 * 2 < 3) or not(2*2 <2)
    c.) "BUS205" <"BUS205" + "BUS205"
"""
#ANSWER:
#a) true
#b) true
#c) true

#Q2
""" 
Write a program that takes a single integer as an argument and prints "This number is divisible by three."
if the argument is divisible by 3 and "This number is not divisible by three." otherwise.
"""
x = int(input("Please enter a number: "))
number = x%3
if number==0:
    print("This number is divisible by three")
else:
    print("This number is not divisble by three")
#ANSWER
#Please enter a number: 9
#This number is divisble by three
#Please enter a number: 7
#This number is not divisble by three

#Q3
"""
Write a program to process a savings account withdrawal.The program should request the current balance and the
amount of withdrawal as input and then display the new balance. If the withdrawal is greater than the original
balance, the program should display "Withdrawal denied". If the new balance is less than $150, the message
"Balance below $150 should also be displayed".
"""
currentBalance = eval(input("Please enter current balance: "))
withdrawalAmount = eval(input("Please enter withdrawal balance: "))
newBalance = currentBalance - withdrawalAmount

if withdrawalAmount>currentBalance:
    print("WITHDRAWAL DENIED")
elif newBalance < 150:
    print("New balance:" , newBalance)
    print("BALANCE BELOW 150")
else:
    print("New balance:" , newBalance)

#Q4

"""
A copy center charges 7 cents per copy for first 100 copies and 5 cents for each additional copy.Write a program
that requests the user the number of copies and displays the total cost of the copies.
"""
copyTotal = int(input("Please enter the number of copies: "))
copyCost = 0.07*copyTotal

if copyTotal > 100:
    #100 copies @ 7 cents=$7
    print(7+((copyTotal - 100)*0.05)) 
else:
    print(copyCost)

#Q6)
"""write a program that requests a positive integer, checks if the integer is greater than 1 and factors it into
#a product of prime numbers. Note, a number is prime if it only factors are 1 and itself.
"""
n=eval(input("Please enter an integer that is greater than 1: "))
i=2
factors=[]
while i*i<=n:
    if n%i:
        i+=1
    else:
        n//=i
        factors.append(i)
if n>1:
    factors.append(n)
print(factors)

#ANSWER:
#Please enter an integer that is greater than 1: 6
#[2, 3]


#Q7)
An annuity of equal periodic payments. one type of annuity is called a savings plan, consists of monthly payments into savings account in order to generate 
#money for a future purchase. suppose you decide to deosit a $100 at the end of each month into a savings account paying 3% interest compounded monthly.
#the monthly interest will be (0.0025) and the balance in the account at the end of each month will be
#
#(balance at end of month) = 1.0025 *(balance at end of previous month) + 100
#after how many months will the account contain less thant $600, and what will be the amount in the account at that time?
bankAccount = 0
month = 0
while bankAccount <600:
    bankAccount += 100
    bankAccount *= 1.0025
    if bankAccount >=600:
        print("After", month, "months the account will contain more than $600. At" , month , "months, the account will contain" , round(bankAccount,2))
        break
    month +=1
    print("Month", month, "balance is", "$",round(bankAccount,2))
    

#ANSWER:
#Month 1 balance is $ 100.25
#Month 2 balance is $ 200.75
#Month 3 balance is $ 301.5
#Month 4 balance is $ 402.51
#Month 5 balance is $ 503.76
#The account will contain less than $600 for 5 months. In the 5th month, the amount in account is $503.76.


#Q8) write a menu-driven program that allows the user to make transactions to a saving account. assume that the account initially has a balance of $1,000.
#
#the menu is:
#    1- make a deposit
#    2- make a withdrawal 
#    3- Obtain balance
#    4- quit
#
#the program should act as follows:
#    make a selection from menu: 1
#    enter amount of deposit: 500
#    deposit processed
#    make a selection from menu: 2
#    enter amount to withdraw: 5000
#    Denied. Maximum withdrawal is $1000
#    enter amount of withdrawal: 600
#    withdrawal processed.
#    make a selection from the options menu: 3
#    balance is $400
#    make a selection from menu: 4

balance=1000
print("Make a selection from the menu:\n1. Make a deposit\n2. Make a withdrawl\n3. Obtain balance\n4. Quit")
selection=int(input("What is your Selection: "))
while True:
    if selection==1:
        deposit=int(input("Enter the amount you'd like to deposit: "))
        balance+=deposit
        print("Deposit processed.")
        break
    elif selection==2:
        withdraw=int(input("Enter the amount you'd like to withdraw: "))
        if withdraw>balance:
            print("Withdraw denied, maximum withdrawl amount is",balance,"dollars.")
            break
        else:
            print("Withdrawl processed.")
            break
    elif selection==3:
        print("Balance is $400 dollars.")
        break
    else:
        break

