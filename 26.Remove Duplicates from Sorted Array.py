# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 17:44:00 2020

@author: Caven
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        read = 0
        write = 0
        while read < n:
            if nums[read] == nums[write]:
                read +=1
            else:
                write +=1
                nums[write] = nums[read]
                
        return write +1