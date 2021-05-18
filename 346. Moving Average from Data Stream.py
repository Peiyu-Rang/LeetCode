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
        
        self.queue = [0] * size
        self.count = 0
        self.capacity = size
        self.total = 0
        self.head = 0
        self.tail = 0
        

    def next(self, val: int) -> float:
        if self.count < self.capacity:
            self.queue[self.tail % self.capacity] = val
            self.tail +=1
            self.count +=1
            self.total += val
            return self.total / self.count
        else:
            self.total -= self.queue[(self.tail) % self.capacity]
            self.queue[(self.tail) % self.capacity] = val
            self.tail +=1
            self.total += val
            return self.total / self.capacity
        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)