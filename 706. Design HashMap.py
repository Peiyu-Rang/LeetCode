# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 21:47:19 2020

@author: Caven
"""

class MyBucket:
    def __init__(self):
        self.bucket = []
    
    def get(self, key):
        for (i,v) in self.bucket:
            if i ==key:
                return v
        return -1
    
    def put(self, key, value):
        found = False
        for i, v in enumerate(self.bucket):
            if key == v[0]:
                self.bucket[i] = (key, value)
                found =True
                break
        
        if not found:
            self.bucket.append((key,value))
            
    def remove(self, key):
        for i,v in enumerate(self.bucket):
            if key == v[0]:
                self.bucket.pop(i)

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keySpace = 2069
        self.hashTable = [MyBucket() for i in range(self.keySpace)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hashKey = key%self.keySpace
        self.hashTable[hashKey].put(key, value)
        
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hashKey = key%self.keySpace
        return self.hashTable[hashKey].get(key)

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hashKey = key%self.keySpace
        self.hashTable[hashKey].remove(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)