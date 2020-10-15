# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 15:15:13 2020

@author: Caven
"""


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        buff = []
        ans = {}
        for item in nums2:
            while buff and buff[-1] < item:
                ans[buff.pop()] = item
            buff.append(item)
            
        return [ans.get(x, -1) for x in nums1]