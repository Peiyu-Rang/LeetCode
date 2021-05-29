# -*- coding: utf-8 -*-
"""
Created on Sat May 29 13:41:03 2021

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
                
                if i < size -1:
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
        
        left_most = root
        
        while left_most.left:
            head = left_most
            
            while head:
                head.left.next = head.right
                
                if head.next:
                    head.right.next = head.next.left
                    
                head = head.next
                
            left_most = left_most.left
            
        return root