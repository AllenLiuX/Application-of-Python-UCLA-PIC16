# import time
# print(time.process_time())
# x = (3,'a',[1,2,3],{'A':1, 'B':2})
# a,b,c,d = x # tuple unpacking
# print(b)
# print(x[2])
# # raise TypeError("hi there")
# while a<10000:
#     a = a+1
#
# print(time.process_time())

# class A(object):
#     def __init__(self):
#         print("initing A")
#         self.a = 0
#     def method(self):
#         print("A method")
# class B(A):
#     def __init__(self, b):
#         print("initing B")
#         print(b)
#         super(B, self).__init__()
#         print(self.a)
#
# b = B(1)
# b.method()
# # super(B, B).__init__()
# print(b.a)


# s="aba"
# s = s.replace('a','c')
# print(s)

import numpy as np
import matplotlib.pyplot as plt

# plt.plot([1,2,3,4],[1,4,9,16],'g^')
# plt.show()

x = np.arange(0,20,0.5)
print(type(x))
y = x.reshape(2,4,-1)
print(y)
print(y.ndim,y.shape)
mask1 = x<= 8
print(x[mask1])

i = np.random.permutation(y)
print(i)
i[:]=1
print(i)