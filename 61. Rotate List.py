# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 22:30:29 2021

@author: Caven
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        n = 1
        
        if not head:
            return head
        
        p = head
        while p.next:
            n +=1
            p = p.next
            
        p.next = head
        
        
            
        cut = n - k%n - 1
        p = head
        for i in range(cut):
            p = p.next
            
        new_head = p.next
        
        p.next = None
        
        return new_head