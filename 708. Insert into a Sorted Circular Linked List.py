# -*- coding: utf-8 -*-
"""
Created on Wed May 12 23:22:09 2021

@author: Caven
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if head is None:
            new_node = Node(insertVal)
            new_node.next= new_node
            return new_node
        
        prev, curr = head, head.next
        
        to_insert = False
        
        while True:
            if prev.val <= insertVal <= curr.val:
                to_insert = True
            elif prev.val > curr.val:
                if insertVal >= prev.val or insertVal <= curr.val:
                    to_insert = True
            
            if to_insert:
                prev.next = Node(insertVal, curr)
                return head
            
            prev, curr = curr, curr.next
            
            # loop condition:
            if prev == head:
                break
            
        prev.next = Node(insertVal, curr)
        return head