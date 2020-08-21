# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 08:30:26 2020

@author: Caven
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        else:
            slow = head
        if head.next is None:
            return False
        else:
            fast = head.next
        while(slow != fast):
            if (fast is None or fast.next is None):
                return False
            slow = slow.next
            fast = fast.next.next
        return True