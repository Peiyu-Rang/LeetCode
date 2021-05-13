# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 22:22:49 2020

@author: Caven
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        g10 = 0
        preH = ListNode()
        p = preH
        
        while l1 or l2:
            if l1:
                x = l1.val
            else:
                x = 0
            
            if l2:
                y = l2.val
            else:
                y = 0
            
            total = g10 + x + y
            g10 = total // 10
            
            p.next = ListNode(total % 10)
            p = p.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        
        if g10 > 0:
            p.next = ListNode(g10)
        
        return preH.next