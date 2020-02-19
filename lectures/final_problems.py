"""Problem 1: Given an integer n, count the total number of digit 1 appearing in all non- negative integers less than or equal to n.
 For example, given n = 13, return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
"""

def count_1(n):
    res = 0
    for i in range(n+1):
        for c in str(i):
            if c=='1':
                res += 1
    return res
print count_1(110)

"""Problem 2: Write a function that takes a directed network in the form of an adjacency matrix as input (numpy array)
 and outputs the same network in the form of a dictionary with entries x:y for each edge xy.
"""

import numpy as np
def edge_dict(mat):
    dict = {}
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            if mat[i][j] != 0:
                dict[i] = j
    return dict

mat = np.array([[1,0,1],[0,1,0],[1,0,1]])
print edge_dict(mat)

"""Problem 3: Use Tkinter to write a function that shows a filled square that changes color each time the user clicks inside it.
"""
import tkinter as tk
import random as rand

def rectangle():
    root = tk.Tk()
    canvas = tk.Canvas(root,width=200, height=200)
    canvas.pack()
    color = ['red','blue','green','purple','black','white','pink']
    def rec(ev):
        canvas.create_rectangle(20, 20, 180, 180, fill=color[rand.randint(0,len(color)-1)])
    canvas.bind("<Button-1>", rec)    #!!!
    root.mainloop() #!!!

# rectangle()

"""Problem 4: Write a function that uses a regular expression to find all IP addresses in a piece of text (input as a single string). The function will return a list of all IP addresses. If the same IP address appears multiple times, only one should be reported.
"""
import re
def find_IP(str):
    pat = re.compile(r'((?:[0-9]{1,3}\.)[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})')
    res = re.findall(pat, str)
    res = list(set(res))
    for ip in res:
        temp = ""
        valid =  True
        for i in ip:
            if i=='.':
                if int(temp)>255:
                    valid = False
                    break
                temp=''
            else:
                temp+=i
        if not valid:
            res.remove(ip)
    return res

print find_IP("123.1.34.32 asd12.43.213.225.dsfsd.12.43.213.225 256.12.123.12")

"""Problem 5: Write a sorting algorithm that sorts a list as follows: 
it goes through the list until it finds the first element less than its predecessor. 
It then takes this element out, and goes through the list from the beginning again, and drops the element in the right place. 
It repeats until there are no more such elements. So, one step would turn the list [1,3,5,4,2] into [1,3,4,5,2].
"""

# def add(li):
#     li.append(1)
#     return li
# li = [1,2,3,4]
# li2 = add(li)
# print li2, li

def mysort(li):
    done = False
    while True:
        n = len(li)
        for i in range(1,n):
            if li[i]<li[i-1]:
                temp = li[i]
                li.pop(i)
                for j in range(n):
                    if temp<=li[j]:
                        li.insert(j,temp)
                        # print li,n
                        break
                # print "here1"
                break
            # print i,n
            if i==n-1:
                done=True
                break
        if done:
            break
    return li

li = [1,3,5,4,2]
# li2 = li.sort()
print li
print mysort(li)