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
        arr = []
        while(head):
            arr.append(head.val)
            head = head.next
            
        n = len(arr)
        i = 0
        j = n-1
        if n < 2:
            return True
        while(i < j):
            if arr[i] != arr[j]:
                return False
            i +=1
            j -=1
        
        return True