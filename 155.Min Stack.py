# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 21:11:58 2020

@author: Caven
"""

class MinStack:
    def __init__(self):
        self.stack = []
    
    def push(self, x: int) ->None:
        if len(self.stack) == 0:
            self.stack.append((x,x))
        else:
            if x < self.stack[-1][1]:
                self.stack.append((x,x))
            else:
                self.stack.append((x, self.stack[-1][1]))
    
    def pop(self) -> None:
        self.stack.pop()
    
    def top(self) ->int:
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1][0]
    
    def getMin(self) -> int:
        return self.stack[-1][1]