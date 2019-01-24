# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 14:10:13 2019

@author: deepajha
"""

#Given a string and a non-negative int n, return a larger string that is n copies of the original string.
# Printing the ntimes the given string in the function. 

#
def times_str(string, n):
    result = "" # Defines it to string for the program
    for i in range(n): # Range makes it to print it from 1 to the natural numbers. 
        result = result + string
    return result 
###################
    
# Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front.

def front_char(front_char, n):
    first_3 = ""
    first_3 = front_char[1:3]
    for i in range(n):
        first_3 = first_3 + n
        return front
    
    
#
        
def front_char(string, n )
    length = 3
    if length > len(string) :
        length = len(string)
    front 
 ###############


# Printing for the values for in decreasing manner

def splosion(string):
    result = ""
    length = len(string)
    
    for i in range(length):
        result = result + string[:i+1]
    return result
    
    
    
    

   