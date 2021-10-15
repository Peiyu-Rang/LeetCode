# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 19:48:23 2021

@author: Caven
"""


class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.bucket = []
        self.maxStack = []
        

    def push(self, x):
        self.bucket.append(x)
        
        if len(self.maxStack) == 0:
            self.maxStack.append(x)
        elif x >= self.maxStack[-1]:
            self.maxStack.append(x)

    def pop(self):
        if len(self.bucket) == 0:
            return None
        topNum = self.bucket.pop()
        if self.maxStack[-1] == topNum:
            self.maxStack.pop()
        return topNum

    def top(self):
        return self.bucket[-1]

    def peekMax(self):
        if len(self.maxStack) == 0:
            return None
        return self.maxStack[-1]

    def popMax(self):
        maxNum = self.maxStack.pop()
        
        b = []
        while(self.bucket[-1] != maxNum):
            b.append(self.bucket.pop())
            
        self.bucket.pop()
        
        while(b):
            self.push(b.pop())
        
        
        return maxNum
 
# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()