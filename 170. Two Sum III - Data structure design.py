# -*- coding: utf-8 -*-
"""
Created on Mon May 17 17:43:47 2021

@author: Caven
"""


class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        
        

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.data.append(number)
        
        

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        self.dic = {}
        for i,v in enumerate(self.data):
            if value - v in self.dic:
                return True
            else:
                self.dic[v] = i
            
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)