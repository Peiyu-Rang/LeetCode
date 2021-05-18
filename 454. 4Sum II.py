# -*- coding: utf-8 -*-
"""
Created on Mon May 17 18:25:16 2021

@author: Caven
"""


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        dic = {}
        res = 0
        for i in nums1:
            for j in nums2:
                if i + j in dic:
                    dic[i + j] +=1
                else:
                    dic[i + j] = 1
        
        for i in nums3:
            for j in nums4:
                if -i - j in dic:
                    res +=dic[-i-j]
                
                
        return res