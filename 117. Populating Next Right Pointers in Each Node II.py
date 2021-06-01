# -*- coding: utf-8 -*-
"""
Created on Sat May 29 14:00:33 2021

@author: Caven
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        q = deque([root])
        
        while q:
            size = len(q)
            
            for i in range(size):
                node = q.popleft()
                
                if i < size - 1:
                    node.next = q[0]
                else:
                    node.next = None
                    
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
                    
        return root
    
    
class Solution:
  
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        head = None
        prev = None
        curr = root
        
        while curr:
            while curr:
                if curr.left:
                    if not head:
                        head = curr.left
                        prev = curr.left
                    else:
                        prev.next = curr.left
                        prev = prev.next
                        
                if curr.right:
                    if not head:
                        head = curr.right
                        prev = curr.right
                    else:
                        prev.next = curr.right
                        prev = prev.next
                        
                curr = curr.next
                
            curr = head
            head = None
            prev = None
            
        return root