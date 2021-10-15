# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 01:23:23 2021

@author: Caven
"""


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
            
        target_sum = total_sum // k
        
        nums.sort(reverse = True)
        
        taken = [False] * n
        
        def backtrack(idx, count, curr_sum):
            if count == k-1:
                return True
            
            if curr_sum > target_sum:
                return False
            
            if curr_sum == target_sum:
                return backtrack(0, count + 1, 0)
            
            for i in range(idx, n):
                if not taken[i]:
                    taken[i] = True
                    
                    if backtrack(i + 1, count, curr_sum + nums[i]):
                        return True
                    
                    taken[i] = False
                    
            return False
        
        return backtrack(0,0,0)