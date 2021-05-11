# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 22:02:43 2020

@author: Caven
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                p = head
                while p != slow:
                    p = p.next
                    slow = slow.next
                    
                return p