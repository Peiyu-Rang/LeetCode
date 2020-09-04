# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 16:30:33 2020

@author: Caven
"""

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow