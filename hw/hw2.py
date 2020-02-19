#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: Wenxuan Liu
"""

from math import *

"""
Traverse the dictionary to use each key as a head. 
For each head, go along the dictionary by use the head's value as the next key, 
and the next key's value as its next key, and so on.
Use an int to compare and store the highest value.
"""
def longestpath(d):
    """
    finds the length of the longest path, (a : b) → (b : c) → ···, in a dictionary d.
    """
    hi = 0  #to store the maximum value of the length
    for key, value in d.items():
        cur = 1
        apd = [key] #use an array to store the keys that has been used
        while(d.has_key(value) and not value in apd):
            cur += 1
            apd.append(value)
            value = d[value]
        if cur > hi:    #set the maximum value if there is a bigger one
            hi = cur
    return hi

##Test Cases:
# d1 = {"a":"b","b":"c"}
# d2 = {"a":"b","b":"c","c":"d","e":"a","f":"a","d":"b"}
# print longestpath(d1)
# print longestpath(d2)

"""
while f(x) is greater than the tolerance, repeatedly calculate the f(x) each time we has a root x.
In the loop, compare f(x) with the tolerance, if f(x) is greater, calculate the next root with Newton's method. 
"""
def solve(f,x0,t):
    """
    find a root (zero) of a function with Newton's method
    """
    root = x0
    dif = t+1   #initialize dif so that it can get into the loop
    while dif > t:
        dif = abs(f(root)[0])   #dif is f(x0)
        if dif <= t:
            return root #return immediately if f(x0) is less or equal to the tolerance(t)
        f1 = float(f(root)[0])  #change the type into float so that the division will not be rounded
        f2 = float(f(root)[1])
        root = root-(f1/f2) #find the next x
    return root

print solve(lambda x: [x**2-1, 2*x], 3, 0.0001)         #correct, the answer should be 1
print solve(lambda x: [x**2-1, 2*x], -1, 0.0001)        #correct, the answer should be -1
print solve(lambda x: [exp(x)-1, exp(x)], 1, 0.0001)    #correct, the answer should be 0
print solve(lambda x: [sin(x), cos(x)], 0.5, 0.0001)    #correct, the answer should be 0