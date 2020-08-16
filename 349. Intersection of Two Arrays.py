# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 15:44:03 2020

@author: Caven
"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return set.intersection(set1,set2)