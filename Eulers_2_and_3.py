# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 09:32:39 2019

@author: deepajha
"""

# Only for testing 

score = 12
if score >= 90:
    grade = 'a'
elif score >=80:
    grade = 'b'
else:
    grade = 'f'
    
#######################
    
band1_names = ['John', 'George', 'Paul', 'Ringo']
band2_names = ['Paul']
names_to_bands = {}
for name in band1_names:
    names_to_bands.setdefault(name,
                              []).append('Beatles')
for name in band2_names:
    names_to_bands.setdefault(name,
                             []).append('Wings')
print(names_to_bands['Paul'])

#########

def default_parameter(num, n=3):
    return num + n

#############
    
# Negative indexing in a list 
    
class Robot:
    def intoduce_self(self, name):
        print("My name is" + self.name)


################
# Building the test classes for the employee 

class Employee:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last 
        self.salary = salary
        self.email = 'first' + 'last' + '@domain.com'
    
    def full_name(self):
        return '{} {}'.format(self.first, self.last)


emp1 = Employee('test','name', 400)



##########################

# Sum of even fibonacci numbers till 4,000,0000

a, b = 1, 1
total = 0 
while a<=4000000:
    if a%2 == 0:
        total +=a
    a, b = b, a+b
#print a

print(total)
###################

# The prime factors of 13195 are 5, 7, 13 and 29.

""" What is the largest prime factor of the number 600851475143 ?
"""
prime = 600851475143
    
for i in range(1,prime):
    if prime % i == 0:
        for x in range(2,i):
            if i % x ==0:
                count += 1
                print(count)
        if count ==0:
            list.append(i)
            count =0
print(list)
 
    
    
        