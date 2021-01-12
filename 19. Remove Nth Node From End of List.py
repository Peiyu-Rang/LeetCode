# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 13:37:10 2020

@author: Caven
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        preHead= ListNode()
        preHead.next= head
        
        first = preHead
        second= preHead
        
        for i in range(n+1):
            first = first.next
            
        while first:
            first = first.next
            second = second.next
        
        second.next = second.next.next
        
        return preHead.next
        