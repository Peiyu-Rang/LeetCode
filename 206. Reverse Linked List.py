# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 21:38:44 2020

@author: Caven
"""

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        
        while(curr):
            nextTemp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTemp
            
        return prev