# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 22:40:13 2021

@author: Caven
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = head
        
        while curr:
            prev = dummy
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
                
            next_node = curr.next
            curr.next = prev.next
            prev.next = curr
            curr = next_node
            
        return dummy.next