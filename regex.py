import re

def func(v):
    v1 = str(v)
    a = re.search(r'abc', 'abcd').group()
    b = re.search(r'abc', v1).group()
    isInt = re.search(r'\d+','abcd123').group()
    return b

# print func('abcd')
page = """hangjie@math.ucla.edu
hangjie AT math DOT ucla DOT edu 
hangjie at math dot ucla dot edu 
hangjie[AT]ucla[DOT]edu 
hangjie[at]ucla[dot]edu
abc@123.asd dot asd"""
mails = re.findall(r'([0-9a-zA-Z]+[\[| ]?(?:@|at|AT)[\]| ]?[0-9a-zA-Z]+(?:[\[| ]?(?:\.|dot|DOT)[\]| ]?[a-z0-9A-Z]+){0,})', page)
mails2 = re.finditer(r'[0-9a-zA-Z]+(@| at | AT |\[at\]|\[AT\])[0-9a-zA-Z]+((\.| dot | DOT |\[dot\]|\[DOT\])[a-z0-9A-Z]+){0,}', page)
print type(mails2)
res = []
for i in mails2:
    res.append(i.group())
print res
print mails