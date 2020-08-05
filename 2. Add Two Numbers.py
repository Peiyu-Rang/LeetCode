# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 22:22:49 2020

@author: Caven
"""

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res =temp = ListNode()
        lt10 = 0
        
        while (l1 is not None) or (l2 is not None) or (lt10 > 0):
            if l1:
                v1 = l1.val
            else:
                v1 = 0
            if l2:
                v2 = l2.val
            else:
                v2 = 0

            digitSum = v1 + v2 + lt10
            if digitSum >= 10:
                temp.val = digitSum % 10
                lt10 = 1
            else:
                temp.val = digitSum
                lt10 = 0

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            if (l1 is not None) or (l2 is not None) or (lt10 > 0):
                temp.next = ListNode()
                temp = temp.next
            else:
                break
        
        return res