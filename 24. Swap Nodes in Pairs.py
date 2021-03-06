# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 09:08:00 2021

@author: Caven
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        p = head
        new_start = p.next
        
        while True:
            q = p.next
            temp = q.next
            
            q.next = p
            
            if not temp or not temp.next:
                p.next = temp
                break
                
            p.next = temp.next
            
            p = temp
        
        return new_start
    
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        first = head
        second = head.next
        
        first.next = self.swapPairs(second.next)
        second.next = first
        
        return second