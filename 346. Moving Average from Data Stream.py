# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 15:38:01 2020

@author: Caven
"""


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.win = []
        

    def next(self, val: int) -> float:
        self.win.append(val)
        n = len(self.win)
        if n < self.size:
            return 1.0*sum(self.win)/n
        else:
            self.win = self.win[-self.size:]
            return 1.0*sum(self.win)/self.size
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)