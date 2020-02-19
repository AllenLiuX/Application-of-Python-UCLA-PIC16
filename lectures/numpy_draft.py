from numpy import *

m1 = mat([[1,0,0,0],[0,1,0,0],[0,0,4,0],[0,0,0,1]])
m2 = mat([[1,0,0,1],[0,1,0,2],[0,0,1,0],[0,0,0,1]])
v1 = mat([[1],[3],[5],[10]])
print(m1)
print(m2)
print(m1*m2)
print(m2*m1)
print(m1*m2*v1)
print(m2*m1*v1)