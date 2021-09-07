# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 22:33:33 2021

@author: Caven
"""


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        dic = {}
        l = len(nums)
        s = 0
        dic[0]=-1

        for i in range(0, l):
            s+=nums[i]
            if s%k in dic: 
                if i-dic[s%k]>=2:
                    return True
            else:
                dic[s%k] = i
        return False