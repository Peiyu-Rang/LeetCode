# -*- coding: utf-8 -*-
"""
Created on Mon May 10 23:09:27 2021

@author: Caven
"""


class ListNode:
    def __init__(self, x = 0):
        self.val = x
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.head = ListNode(0)
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        
        if index < 0 or index >= self.size:
            return -1
        
        cur = self.head
        for i in range(index + 1):
            cur = cur.next
            
        return cur.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        
        self.addAtIndex(self.size, val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.size or index < 0:
            return
        
        self.size +=1
        
        pred = self.head
        
        for i in range(index):
            pred = pred.next
            
        new_node = ListNode(val)
        new_node.next = pred.next
        pred.next = new_node
        
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        
        if index >= self.size or index < 0:
            return 
              
        
        pred = self.head
        for i in range(index):
            pred = pred.next
        
        if index + 1 != self.size:
            print(index)
            print(self.size)
            pred.next = pred.next.next
        else:
            pred.next = None
            
        self.size -=1