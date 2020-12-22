# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 22:12:42 2020

@author: Caven
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        before = before_head = ListNode()
        after = after_head = ListNode()
        
        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            
            head = head.next
            
        
        after.next = None
        before.next = after_head.next
        
        return before_head.next