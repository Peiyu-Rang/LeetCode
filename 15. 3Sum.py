# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 23:02:05 2020

@author: Caven
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            elif i == 0 or nums[i-1] != nums[i]:
                self.twoSum(nums,i,res)
        
        return res
        
        
    def twoSum(self, nums, i, res):
        low = i+1
        high = len(nums)-1
        
        while low < high:
            total = nums[i] + nums[low] + nums[high]
            if total < 0:
                low +=1
            elif total >0:
                high -=1
            else:
                res.append([nums[i], nums[low], nums[high]])
                low +=1
                high -=1
                while low < high and nums[low] == nums[low -1]:
                    low +=1
                    
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = set()
        for i in range(n-2):
            left = i + 1
            right = n-1
            
            a = nums[i]
            
            while left < right:
                if a + nums[left] + nums[right] == 0:
                    res.add((a, nums[left], nums[right]))
                    left +=1
                elif a + nums[left] + nums[right] > 0:
                    right -=1
                else:
                    left +=1
        
        
        return list(res)
                
            
            
        
            