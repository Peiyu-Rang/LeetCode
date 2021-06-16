# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 22:33:18 2020

@author: Caven
"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # time O(N)
        '''
        from collections import Counter
        
        counterNums = Counter(nums)
        
        for key in counterNums:
            if counterNums[key] > 1:
                return key
        '''
        
        # space O(1)
        
        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
                
        p1 = nums[0]
        p2 = slow
        while p1 != p2:
            p1 = nums[p1]
            p2 = nums[p2]

        return p1
    
    
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for key in counter:
            if counter[key] > 1:
                return key