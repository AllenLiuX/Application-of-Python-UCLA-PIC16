#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: Wenxuan Liu
"""

import random

"""
    Use "for" loop to process each element in the list, and use if/elif/else to process each element in different cases.
"""
def largerIndex(c):
    """
     Takes a list as input and return a new list k. For each element in the new list, k[i] = 1 if c[i] > i, k[i] = 0 if c[i] = i, k[i] = -1 if c[i] < i.
    """
    k = []
    a = 0
    for i in c:
        if i > a:
            k.append(1)
        elif i == a:
            k.append(0)
        else:
            k.append(-1)
        a = a+1
    return k

"""
    use while loop to increment i and append i*i to the new list each time.
"""
def squareUpTo(n):
    """
    Takes as input a positive integer n, and returns a list of all the square numbers up to (and possibly including) n.
    """
    i = 1   #should be i = 0
    b = []
    while i**2 <= n:    #increase i*i until it equals to n
        b.append(i**2)
        i = i+1
    return b

"""
    Coins A and B are flipped in turns, if A firstly has the head, return False immediately; if B firstly has the head, return True immediately. Otherwise begin again. 
    Let A flips at the beginning, it has 1/2 chance to return False, and then B has 1/4 chance to return True. Then, A has 1/8 and B has 1/16...
    In all, A has 1/2+1/8+1/32+..., and B has 1/4+1/16+1/64+.....
    Therefore, A totally has 2/3 chance to return False, and B has 1/3 chance to return True. 
"""
def flip1in3():
    """
    this function returns False with probability 2/3 and returns True with probability 1/3.
    """
    while(True):
        a = random.randint(1,2) #two fair coins.
        b = random.randint(1,2)
        if a == 1:
            return False
        if b == 1:
            return True


"""
use for loop to traverse the list from the beginning to the end.
For each element, traverse the elements come after it, and see if there is an element same to it. If so, append it to the new list.
"""
def duplicates(c):
    """
    Some elements appear twice and others appear once.
    The function outputs all the elements as a list that appear twice in the list c.
    The elements in the output should preserve the original order.
    """
    a = 1
    l = []
    s = len(c)
    for i in range(0, s-1):
        for j in range(i+1, s):
            if c[j] == c[i]:
                l.append(c[j])
                break
        a = a+1
    return l

##test cases:
##test1
# l1 = [1,2,0,4,2,1,40,-5]
# l2 = [0,3,2,1,32,3,4,0]
# print largerIndex(l1)
# print largerIndex(l2)
#
##test2
# print squareUpTo(10)
# print squareUpTo(100)
#
##test3
# x=y=0
# for i in range(20000):
#     a = flip1in3()
#     if a:
#         x = x+1
# print x
#
##test4
# l3 = [1,2,5,3,6,2,4,5]
# l4 = [1,3,5,5,1,4,3]
# print duplicates(l3)
# print duplicates(l4)