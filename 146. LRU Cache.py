# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 20:57:07 2020

@author: Caven
"""

class DoubleLinkedNode():
    def __init__(self, key = 0, value= 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.size = 0
        self.head = DoubleLinkedNode()
        self.tail = DoubleLinkedNode()
        
        self.head.next = self.tail
        self.tail.prev = self.head

    
    def moveToHead(self,node):
        self.removeNode(node)
        self.addNode(node)
    
    def removeNode(self,node):
        prevNode = node.prev
        nextNode = node.next
        
        prevNode.next = nextNode
        nextNode.prev = prevNode
        
    def addNode(self, node):
        # alway add node right after head
        node.prev = self.head
        node.next = self.head.next
        
        self.head.next.prev = node
        self.head.next = node
    
    def popTail(self):
        tail = self.tail.prev #?
        self.removeNode(tail)
        return tail
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.moveToHead(node)
        
        return node.value
    
    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = DoubleLinkedNode(key, value)
            self.cache[key] = node
            self.addNode(node)
            
            self.size +=1
            if self.size > self.capacity:
                # pop the tail
                tail = self.popTail()
                del self.cache[tail.key]
                self.size -= 1
        
        else:
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)
            
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)