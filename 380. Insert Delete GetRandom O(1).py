# -*- coding: utf-8 -*-
"""
Created on Mon May 17 21:42:50 2021

@author: Caven
"""

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bucket = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.bucket:
            return False
        else:
            self.bucket.append(val)
            return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.bucket:
            del self.bucket[self.bucket.index(val)]
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        
        return random.choice(self.bucket)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()