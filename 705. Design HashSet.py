# -*- coding: utf-8 -*-
"""
Created on Sun May 16 20:11:33 2021

@author: Caven
"""


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.content = set()

    def add(self, key: int) -> None:
        self.content.add(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.content.remove(key)
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.content
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)