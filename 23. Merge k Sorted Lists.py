# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 21:53:36 2021

@author: Caven
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pointers = [l for l in lists if l]
        if not pointers:
            return None
        heap = []
        result_head, result_ptr = None, None
        for i, p in enumerate(pointers):
            heapq.heappush(heap, (p.val,i))
            pointers[i] = pointers[i].next
        while heap:
            val, i = heapq.heappop(heap)
            node = ListNode(val, None)
            if not result_head:
                result_head = node
            if result_ptr:
                result_ptr.next = node
            result_ptr = node
            if pointers[i]:
                heapq.heappush(heap, (pointers[i].val, i))
                pointers[i] = pointers[i].next
        return result_head