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
    
    
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set()
        set2 = set()
        res = set()
        for n1 in nums1:
            if n1 not in set1:
                set1.add(n1)
        
        for n2 in nums2:
            if n2 in set1 and n2 not in res:
                res.add(n2)
                
        return list(res)