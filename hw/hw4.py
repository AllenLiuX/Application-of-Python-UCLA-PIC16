#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: Wenxuan Liu 805152602
"""

import re

"""Use regex to seperately match the syntax of int, float, and list, 
   and return the type if matched, otherwise return string."""
def mytype(v):
    """It performs the same action as type(), and can recognize integers, floats, strings, and lists."""
    v1 = str(v)
    isInt = re.search(r'^[\-+]?\d+$', v1)    #if I use ^ or $, I cannot use .group()?
    isFloat = re.search(r'^[\-+]?\d+\.\d+$', v1)
    isList = re.search(r'^\[[\-+]?\d*(, ?[\-+]?\d+)*\]$', v1)
    if isInt:
        return "int"
    if isFloat:
        return "float"
    if isList:
        return "list"
    return "string"

"""Iteratively, first match the syntax for a pdf, then catch the group of name without extension."""
def findpdfs(L):
    """It takes as input a list L of filenames,
       and returns a list of the names of all PDF files, without extension"""
    res = []
    for file in L:
        if(re.search(r'^[0-9a-zA-Z]+\.pdf$', file)):
            name = re.search(r'([0-9a-zA-Z]+)(?=\.pdf)', file).group(1)
            res.append(name)
    return res

import urllib2
"""Match the pattern of email with some options for '@' and '.' in uncatched groups.
   Then, remove the duplicates with set() operation. 
   And use 're.sub' to replace the hidden expressions of '@' and '.'."""
def findemail(url):
    """It takes as input a URL, and outputs any email addresses that look like “xxx@xxx.xxx.xxx”
       with any number of dots after the @-sign on this page.
       It also catches hidden expression of '@' and '.' and translates them."""
    page = urllib2.urlopen(url).read()
    mails = re.findall(r'[0-9a-zA-Z]+(?:@| at | AT |\[at\]|\[AT\])[0-9a-zA-Z]+(?:(?:\.| dot | DOT |\[dot\]|\[DOT\])[a-z0-9A-Z]+){0,}', page)
    temp = list(set(mails))
    res = []
    for str in temp:
        str = re.sub(r'( at | AT |\[at\]|\[AT\])',r'@', str)
        str = re.sub(r'( dot | DOT |\[dot\]|\[DOT\])', r'.', str)
        res.append(str)
    return res

import happiness_dictionary
"""First, use findall to get all the words seperately in the text and store them into a list.
   Then, for each word, add the value of the word in the dictionary if exists.
   Finally, calculate the average value of the words."""
def happiness(text):
    """uses the Dodds et al happiness dictionary to rate the happiness of a piece of english text (input as a single string)"""
    li = re.findall(r'[0-9a-zA-Z]+', text)
    sum = 0.0
    count = 0
    for word in li:
        word = word.lower()
        if(happiness_dictionary.happiness_dictionary.has_key(word)):
            sum += happiness_dictionary.happiness_dictionary[word]
            count += 1
    return sum/count

#testcase 1:
print mytype(10)
print mytype(-1.25)
print mytype([1, 2, 3])
print mytype("abc")

#testcase 2:
res = findpdfs(["IMG2309.jpg", "lecture1.pdf", "homework.py", "homework2.pdf"])
print res

#testcase 3:
url1 = "https://www.math.ucla.edu/~hangjie/contact/"
url2 = "https://www.math.ucla.edu/~hangjie/teaching/Winter2019PIC16/regexTest"
print findemail(url1)
print findemail(url2)

#testcase 4:
s1 = "Mary had a little lamb."
s2 = "Mary had a little lamb. Mary had a little lamb!"
s3 = "A quick brown fox jumps over a lazy dog."
print happiness(s1)
print happiness(s2)
print happiness(s3)


