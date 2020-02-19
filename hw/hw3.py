#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: Wenxuan Liu
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return "%d" % self.data

    def __repr__(self):
        return "%d" % self.data## Test Code:

    def __eq__(self, other):
        """compare the data stored in the node with other, instead of comparing the node itself"""
        return self.data == other

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
        self.first = self.head
        self.last = self.head
        self.n = 1

    def append(self, data):
        """create a new node, make the last node points to this node, and make the last node be the new node"""
        self.n += 1
        temp = Node(data)
        self.last.next = temp
        self.last = temp

    # def __iter__(self):
    #     return self
    #
    # def next(self):
    #     if self.head == None:
    #         self.head = self.first
    #         raise StopIteration
    #     temp = self.head
    #     self.head = self.head.next
    #     return temp.data

    def __iter__(self):
        return self.generator()

    def generator(self):
        """yield each node in the LinkedList from the first to the end"""
        self.head = self.first
        while self.head != None:
            yield self.head
            self.head = self.head.next

    def __len__(self):
        return self.n

    def __str__(self):
        res = "["
        self.head = self.first
        while self.head != None:
            res += "%d->" % self.head.data
            self.head = self.head.next
        res += "]"
        return res

    def __repr__(self):
        return repr(self.__str__())

    def __setitem__(self, key, value):
        self.head = self.first
        cur = 0
        while cur != key:
            self.head = self.head.next
            cur += 1
            if self.head == None:
                print "list index out of range"
                raise IndexError
        self.head.data = value

    def __getitem__(self, item):
        self.head = self.first
        cur = 0
        while cur != item:
            self.head = self.head.next
            cur += 1
            if self.head == None:
                print "list index out of range"
                raise IndexError
        return self.head.data

    def __add__(self, other):
        """Create a new copy of the LinkedList by copying data in each Node to the new Node in the copy in sequence"""
        copy = LinkedList(self.first.data)
        self.head = self.first
        while self.head != None:
            temp = Node(self.head.data)
            copy.n += 1
            copy.last.next = temp
            copy.last = temp
            self.head = self.head.next
        temp = Node(other)
        copy.n += 1
        copy.last.next = temp
        copy.last = temp
        return copy


# a = LinkedList(0);
# a.append(1)
# a.append(2)
# #
# print "7 points if this works"
# for n in a:
#     print n
#
# print ""
#
# print "2 points if this works"
# for n in a:
#     print n
#
# print ""
#
# print "3 points if both of these work"
# for n in a:
#     if n == 2:
#         break
#     else:
#         print n
#
# print ""
#
# for n in a:
#     if n == 2:
#         break
#     else:
#         print n
#
# print ""
#
# a.append(3)
# a.append(4)
# a.append(5)
# a.append(6)
# a.append(7)
# a.append(8)
#
# print ""
#
# print "1 points if this works"
# print len(a)
# print ""
# #
# print "1 points if this works"
# print str(a)
# print ""
#
# print "1 points if this works"
# print repr(a)
# print ""
# #
# print "1 points each. That is, 2 points if the output of the next line is correct"
# a[5] = 20
# print a[5]
#
# print ""
#
# print "2 points for correct operation of +"
# a + 9  # doesn't modify a
# print a
#
# print ""
#
# a = a + 9  # appends 9 to a
# print a
#
# print ""
#
# print "1 points for raising correct IndexError"
# try:
#     print a[999]
# except IndexError as e:
#     print e
# #
# # print ""
# #
# # print ""
# # print "-----"
# # print ""
# # print "Example output:"
# # print """
# # 7 points if this works
# # 0
# # 1
# # 2
# #
# # 2 points if this works
# # 0
# # 1
# # 2
# #
# # 3 points if both of these work
# # 0
# # 1
# #
# # 0
# # 1
# #
# #
# # 1 points if this works
# # 9
# #
# # 1 points if this works
# # [0->1->2->3->4->5->6->7->8->]
# #
# # 1 points if this works
# # '[0->1->2->3->4->5->6->7->8->]'
# #
# # 1 points each. That is, 2 points if the output of the next line is correct
# # 20
# #
# # 2 points for correct operation of +
# # [0->1->2->3->4->20->6->7->8->]
# #
# # [0->1->2->3->4->20->6->7->8->9->]
# #
# # 1 points for raising correct IndexError
# # list index out of range
# #
# # """