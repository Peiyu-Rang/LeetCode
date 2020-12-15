# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 21:06:10 2020

@author: Caven
"""

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        left = 0
        right = 0
        Sum = nums[0]
        ans = float('Inf')
        
        while (left <= n-1 and right <= n-1):
            if Sum < s:
                if right < n-1:
                    right +=1
                    Sum += nums[right]
                else:
                    break
            else:
                if right - left +1 < ans:
                    ans = right - left +1
                else:
                    Sum -= nums[left]
                    left +=1
                    
                    
        return 0 if ans == float('Inf') else ans
            
        
        
        '''
        n = len(nums)
        
        left = 0
        right = 0
        
        ans = float('Inf')
        
        while (left <= n-1 and right <= n-1):
            sub = nums[left:right+1]
            if sum(sub) < s:
                if right <= n-1:
                    right +=1
                else:
                    break
            else:
                if right - left +1 < ans:
                    ans = right - left +1
                left +=1
        
        return 0 if ans == float('Inf') else ans
        '''
        
        '''