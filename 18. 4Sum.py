# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 21:43:09 2020

@author: Caven
"""


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def twoSum(nums, target):
            res = []
            low = 0
            high = len(nums) -1
            while low < high:
                total = nums[low] + nums[high]
                if total < target or (low >0 and nums[low] == nums[low -1]):
                    low +=1
                elif total > target or (high < len(nums)-1 and nums[high] == nums[high+1]):
                    high -=1
                else:
                    res.append([nums[low], nums[high]])
                    low +=1
                    high -=1
            return res
        
        def kSum(nums, target, k):
            res = []
            if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
                return res
            if k == 2:
                return twoSum(nums, target)
            for i in range(len(nums)):
                if i == 0 or nums[i-1] != nums[i]:
                    for _, rest in enumerate(kSum(nums[i+1:], target - nums[i], k-1)):
                        res.append([nums[i]] + rest)
            return res
        
        nums.sort()
        return kSum(nums,target, 4)
        