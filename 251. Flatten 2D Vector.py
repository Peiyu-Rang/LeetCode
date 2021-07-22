# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 01:33:12 2021

@author: Caven
"""


class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.nums = []
        for v in vec:
            for i in v:
                self.nums.append(i)
                
        self.p = -1
        self.length = len(self.nums)

    def next(self) -> int:
        self.p +=1
        if self.p < self.length:
            return self.nums[self.p]
        

    def hasNext(self) -> bool:
        return self.p + 1 < self.length
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()