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
        def getIntersect(head):
            slow = head
            fast = head
            
            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next
                
                if slow == fast:
                    return slow
                
            return None
        
        if head is None:
            return None
        
        intersect = getIntersect(head)
        
        if intersect is None:
            return None
        
        p1 = head
        p2 = intersect
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
            
        return p1