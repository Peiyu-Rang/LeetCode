# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 16:17:24 2020

@author: Caven
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p = m + n -1
        p1 = m-1
        p2 = n-1
        
        while (p >=0):
            if p1 < 0:
                nums1[p] = nums2[p2]
                p2 -=1
            elif p2 < 0:
                nums1[p] = nums1[p1]
                p1 -=1
            elif nums1[p1] <= nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -=1
            else:
                nums1[p] = nums1[p1]
                p1 -=1
            p -=1
                