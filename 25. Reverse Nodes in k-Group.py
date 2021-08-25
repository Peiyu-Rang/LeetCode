# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 23:32:34 2021

@author: Caven
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        ktail = None
        new_head = None
        
        while curr:
            count = 0
            curr = head
            while count < k and curr:
                curr = curr.next
                count += 1
                
            if count == k:
                revHead = self.reverseLinkedList(head, k)
                
                if not new_head:
                    new_head = revHead
                    
                if ktail:
                    ktail.next = revHead
                
                ktail = head
                head = curr
                
        if ktail:
            ktail.next = head
        
        return new_head if new_head else head
    
    def reverseLinkedList(self, head, k):    
        new_head, curr = None, head
        
        while k:
            next_node = curr.next
            
            curr.next = new_head
            new_head = curr
            
            curr = next_node
            
            k-=1
            
        return new_head