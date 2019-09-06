# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 20:50:55 2018

@author: Chase Darlington
"""
####################Quiz6#######################

#Please write your solutions in this script, save as yourname_quiz6_sol.py and upload it on canvas

#Q1
"""
Write a function to calculate the amount of rent to be paid for a car rental service,
assume your function takes two parameters the hourly rate for the car and number of hours the car was used.
Calculate the rent paid as hourlyrate * number of hours used if the number of hours used are less than 6,
else if the rent to be paid should be 250$ if the number of hours used is greater than 6.
Also make sure the number of hours have a limit for only a single day(24hrs).
The function should return the rent to be paid. Also return a sorted list of the values [hourlyrate,number_of_hours].

Ex : Func definition : def rent_paid(hourly_pay,hours):
                         print(total_rent_paid)
						 return sorted_list
                        
     Func call :       rent_paid(pay_per_hour,no_of_hours)
"""

#def rent_total(rate, hours):
#    rent_total=0
#    rent_total=rate*hours
#    print(rent_total)
#rent_total(10,3)

def rent_total(rate, hours):
    if hours<24:
        if hours>6:
            rent = rate * hours
        if hours<=6: #problem states if greater than 6 and if less than 6 scenarios, but not if = 6
            rent=250
        else:
            print('Computational error')
    else:
        print('Invalid input')
        print('Hours greater than 24')
        return False
        
    sorted_list=(rate, hours)
    print('Total Rent (rent to be paid: $' + str(rent))
    return sorted_list

rent_total(10,25)

def rent_total(rate, hours):
    days=hours//24
    remainder=hours%24
    if remainder>6:
        rent = rate * remainder + days * 250
    if remainder<=6: #problem states if greater than 6 and if less than 6 scenarios, but not if = 6
        rent=250 + days * 250
    else:
        print('Computational error')        
    sorted_list=(rate, hours)
    print('Total Rent (rent to be paid: $' + str(rent))
    return sorted_list

rent_total(10,25)
