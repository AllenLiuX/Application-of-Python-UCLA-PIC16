#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: Wenxuan Liu 805152602
"""

import Tkinter as Tk
import sys
import random

class MainScreen:
    def __init__(self, master,n):
        self.master = master
        self.canvas = Tk.Canvas(master, width=700, height=700)
        self.canvas.pack()
        self.side = 500/n
        self.curx = 0
        self.cury = 0
        self.count = 0
        self.first = True
        for i in range(0,n+1):
            self.canvas.create_line(100, 100+i*self.side, 100+n*self.side, 100+i*self.side)
            self.canvas.create_line(100+i*self.side, 100, 100+i*self.side, 100+n*self.side)
        # self.canvas.bind("<Button-1>", self.rectangle)
        color = ['red', 'orange', 'blue', 'yellow']
        for i in range(4):
            color.append(color[i])
            color.append(color[i])
            color.append(color[i])
        self.color2 = []
        while len(color) > 0:
            i = random.randint(0, len(color)-1)
            self.color2.append(color[i])
            color.remove(color[i])
        print(self.color2)
        for i in range(len(self.color2)):
            row = i/4
            col = i%4
            self.canvas.create_rectangle(100+col * self.side, 100+row * self.side, 100+(col+ 1) * self.side, \
                                         100+(row + 1) * self.side, fill=self.color2[i])

        for i in range(9):
            row = i/3
            col = i%3
            self.canvas.create_rectangle(80 + (col+1) * self.side, 80 + (row+1) * self.side, 120 + (col + 1) * self.side, \
                                         120 + (row + 1) * self.side, fill='grey')
        self.canvas.bind("<Button-1>", self.change)

    def change(self, ev):
        if (ev.x-80)%self.side < 40 and (ev.y-80)%self.side < 40 and ev.x < 120 + self.side*3 and ev.y < 120 + self.side*3:
            col = (ev.x-80)/self.side-1
            row = (ev.y-80)/self.side-1
            self.canvas.create_text(20, 20, text=str(col)+str(row))
            nc = [self.color2[col + 4 * row + 4], self.color2[col + 4 * row], self.color2[col + 4 * row + 5], self.color2[col + 4 * row + 1]]
            ul = self.color2[col + 4 * row]
            ur = self.color2[col + 4 * row+1]
            ll = self.color2[col + 4 * row+4]
            lr = self.color2[col + 4 * row+5]
            self.color2[col + 4 * row] = ll
            self.color2[col + 4 * row+1] = ul
            self.color2[col + 4 * row+4] = lr
            self.color2[col + 4 * row+5] = ur
            for i in range(4):
                r = i/2
                c = i%2
                self.canvas.create_rectangle(100+(col+c)*self.side, 100+(row+r)*self.side, \
                                             100+(col+c+1)*self.side, 100+(row+r+1)*self.side, fill = nc[i])

            for i in range(9):
                row = i/3
                col = i%3
                self.canvas.create_rectangle(80 + (col+1) * self.side, 80 + (row+1) * self.side, 120 + (col + 1) * self.side, \
                                             120 + (row + 1) * self.side, fill='grey')






    # def rectangle(self,ev):
    #     tx = int(ev.x/self.side)
    #     ty = int(ev.y/self.side)
    #     if self.first or (abs(tx-self.curx)==1 and abs(ty-self.cury)==2) or (abs(tx-self.curx)==2 and abs(ty-self.cury)==1):
    #         if not self.first:
    #             self.canvas.create_rectangle(self.curx * self.side, self.cury * self.side, (self.curx + 1) * self.side, \
    #                                      (self.cury + 1) * self.side, fill="blue")
    #         self.first = False
    #         self.curx = tx
    #         self.cury = ty
    #         self.canvas.create_rectangle(self.curx*self.side, self.cury*self.side, (self.curx+1)*self.side, \
    #                                      (self.cury+1)*self.side, fill="orange")
    #         self.count += 1
    #         # self.canvas.create_text((self.curx+0.5)*self.side, (self.cury+0.5)*self.side, \
    #         #                         fill="darkblue",font="Times %d italic bold" %(self.side/4), text=str(self.count))
def knightstour(n):
    root = Tk.Tk()
    gui = MainScreen(root, n)
    root.mainloop()

if __name__=='__main__':
    if len(sys.argv)==1:   #pass no argument
        knightstour(4)
    else:
        knightstour(int(sys.argv[1]))   #use the first argument as paremeter to