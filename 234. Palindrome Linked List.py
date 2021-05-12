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
        array = []
        while head:
            array.append(head.val)
            head = head.next
            
        n = len(array)
        l = 0
        r = n-1
        
        while l < r:
            if array[l]!=array[r]:
                return False
            else:
                l +=1
                r-=1
            
        return True