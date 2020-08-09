# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 10:03:09 2020

@author: Caven
"""

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dic = {}
        ans = 0
        for num in nums:
            if num in dic:
                dic[num] +=1
            else:
                dic[num] = 1
        
        print(dic)
        if k == 0:
            for key in dic:
                if dic[key] >=2:
                    ans +=1
        elif k < 0:
            return 0
        else:
            for key in dic:
                if key - k in dic:
                    ans += 1
                
        return ans
                