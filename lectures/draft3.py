# import pandas as pd
# import numpy as np
#
# # f = open('lsd.txt').read()
# # print f
# sd = pd.read_csv("lsd.txt", '\t')
# print(sd)
# print sd.T
# print sd.iloc[2:3]
# print sd.loc[2:3]
# print sd[2:3]
# sd = sd.T
# sd.to_csv("lsd2.csv")

import tkinter as tk
# root = tk.Tk()
# canvas = tk.Canvas(root, width=600, height=600)
# canvas.pack()
# canvas.create_rectangle(0,0,100,100,fill='blue')
# root.mainloop()

# class Main_window:
#     def __init__(self, master):
#         self.master = master
#         self.canvas = tk.Canvas(master, width=600, height=600)
#         self.canvas.pack()
#         self.canvas.bind("<Button-1>",self.func1)
#         self.b1 = tk.Button(master, text='hit me', command=self.hit_me)
#         self.b1.pack()
#     def func1(self, event):
#         self.i=100
#         self.canvas.create_arc(event.x, event.y, event.x+100, event.y+100, start=0, extent=270, fill='red')
#     def hit_me(self):
#         self.canvas.create_text(100,100+self.i,text='hello!')
#         self.b1['state'] = tk.DISABLED
#
# if __name__=='__main__':
#     root = tk.Tk()
#     window = Main_window(root)
#     root.mainloop()

# while True:
#     try:
#         abc=100
#         s = float(input("please enter a number: "))
#         a = 2/s
#         # raise IOError
#     except (IOError,ValueError,ZeroDivisionError) as er:
#         print "sorry try again", er


# for i in range(10):
#     a = 10
#     pass
# def h(d,e):
#     d = 10
#     e[0] = 5
#     e = [1,2]
# b = 2
# a = [1,2,3]
# h(b,a)
# print b #2
# print a #[5,2,3]

# def my_fun(a=10, b=20):
#     print a,b
# my_fun(b=30)
# a=4
# b=5
# print a,b
# print [[i for i in range(1,j)] for j in [2,3,4,5]]

# import re
# reg=re.compile(r'(?<!\w{3})\d')
# res = re.findall(reg,'s2dgv s1 was1as')
# print res
# a = (1,2,3)
# print a[0]

import pandas as pd
import numpy as np
dates = pd.date_range('20191006', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=['A','B','C','D'])
df2 = pd.Series([1,2,3,np.nan, 12,13])
df3 = pd.DataFrame({1:[1,2,3,4],'a':['A','B','C','D']})
print df3
print df
print df.describe()