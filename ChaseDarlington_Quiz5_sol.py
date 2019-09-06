# -*- coding: utf-8 -*-
"""
@author: Al-Abdullah
"""
####################Quiz5#######################

#Please write your solutions in this script, save as yourname_quiz5_sol.py and upload it on canvas

#Q1
"""
Write a program that takes a list of 5 salaries of employees [55000,72000,90000,65000,75000]
and returns the maximum,average of the list using for loops and if constructs only.
**
Do not use any in built functions like sum,max,len.
"""
#PSEUDO CODING

# =============================================================================
# Original
# =============================================================================
salaries=[]
s1=int(100000)
#eval(input("Annual Salary 1: "))
salaries.append(s1)  
n=0
i=0
x=salaries[n]
y=salaries[i]
maximum=[]
minimum=[]
maximum.append(salaries)
minimum.append(salaries)
#for x in range (salaries[0:]):
if (x-y)<=0:
    maximum.remove(x)
while (x-y)>0:
    y+=1
    
print(maximum)

# =============================================================================
# Corrected
# =============================================================================
highest=0
sum1=0
counter=0
salaries=[55000,72000,90000,65000,75000]
for x in salaries:
    if x>highest:
        highest=x
    sum1=sum1+x
    counter=counter+1
    average=sum1/counter
print(average, highest)

highest=0
sum1=0
counter=0
salaries=[5000,4000,12000,2000,3500]
for x in salaries:
    if x>highest:
        highest=x
        lowest=highest
    if x<lowest:
        lowest=x
    sum1=sum1+x
    counter=counter+1
    average=sum1/counter
print(average, highest, lowest)


# =============================================================================
# Sort Function
# =============================================================================

highest=0
salaries=[5000,4000,12000,2000,3500]
for x in salaries:
    if x>highest:
        highest=x
        lowest=highest
    if x<lowest:
        lowest=x
print(highest, lowest)
salaries.remove(lowest)
salaries.append(lowest)
print(salaries)
x=0
for x in salaries:
    if x > lowest:
        salaries.remove(x)
        salaries.append(x)
    x+=1
print(salaries)
    


        
        

#salaries print(max(salaries)) and print(min(salaries)):
#    
#minimum=min(salaries)
#
#print("Maximum:", maximum, "Mininum:", minimum)

    
