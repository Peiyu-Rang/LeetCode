# -*- coding: utf-8 -*-
"""
Created on Wed May 12 22:57:03 2021

@author: Caven
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        
        prev = dummy = Node(None, None, head, None)
        stack = [head]
        
        while stack:
            curr = stack.pop()
            
            prev.next = curr
            curr.prev = prev
            
            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)
                curr.child = None
            
            prev = curr
        
        dummy.next.prev = None
    
        return dummy.next
        