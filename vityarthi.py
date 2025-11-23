# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 16:11:53 2025

@author: srija
"""

n = int(input("Enter a number: "))
num_str = []
result = ""

for i in range(1,n+1):
    result += str(i)
    
for index, digit in enumerate(result, start=1):
    print(f"{index}th digit is {digit} ")
    