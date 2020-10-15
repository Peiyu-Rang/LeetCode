# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 07:21:12 2020

@author: Caven
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        preHead = ListNode()
        preHead.next = head
        
        prev, curr = preHead, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
            
        return preHead.next