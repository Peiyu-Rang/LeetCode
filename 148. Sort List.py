# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 22:57:29 2021

@author: Caven
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        slow, fast = head, head.next
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        start = slow.next
        slow.next = None
        
        l = self.sortList(head)
        r = self.sortList(start)
        
        return self.merge(l, r)
    
    def merge(self,l, r):
        dummy = curr = ListNode()
        while l or r:
            if l and r:
                if l.val < r.val:
                    curr.next = l
                    l = l.next
                else:
                    curr.next = r
                    r = r.next
            elif l:
                curr.next = l
                l = l.next
            else:
                curr.next = r
                r = r.next
                
            curr = curr.next
        
        return dummy.next
        