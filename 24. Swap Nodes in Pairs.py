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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        
        while cur.next and cur.next.next:
            first = cur.next
            sec = cur.next.next
            cur.next = sec
            first.next = sec.next
            sec.next = first
            cur = cur.next.next
        return dummy.next     
        
    
    
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