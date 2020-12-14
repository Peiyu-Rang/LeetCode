# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 22:17:31 2020

@author: Caven
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        cont = []
        while head:
            cont.append(head.val)
            head = head.next
            
        n = len(cont)
        left = 0
        right = n-1
        while left < right:
            if cont[left] != cont[right]:
                return False
            left +=1
            right -=1
            
        return True