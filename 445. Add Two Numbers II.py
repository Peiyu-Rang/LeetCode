# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 22:54:00 2021

@author: Caven
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.reverseLinkedList(l1)
        l2 = self.reverseLinkedList(l2)
        
        carry = 0
        preHead = curr = ListNode()
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            
            total = x + y + carry
            carry = total // 10
            
            curr.next = ListNode(total % 10)
            curr = curr.next
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        if carry > 0:
            curr.next = ListNode(carry)
        
        return self.reverseLinkedList(preHead.next)
    
    
    def reverseLinkedList(self, ll):
        prev = None
        curr = ll
        
        while curr:
            temp = curr.next
            curr.next = prev
            
            prev = curr
            curr = temp
            
        return prev
    
    