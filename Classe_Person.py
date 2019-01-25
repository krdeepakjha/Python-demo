# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 11:34:42 2019

@author: deepajha
"""

# Testing classes 

class Record:
    def __init__(self, name, job = None, pay = 0):
        self.name = name
        self.job = job
        self.pay = pay
        
        
if __name__ == '__main__':
    smith = Record('Paul Smith', job = 'whatever', pay= 10000)
    walter = Record('Charlie Walter', job ='plumber', pay= 30000)
    print(smith.name, smith.pay)
    print(walter.name,walter.pay)
    
    walter.pay *= 1.10
    print('%.2f' % walter.pay)
    