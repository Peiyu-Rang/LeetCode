# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 21:35:47 2021

@author: Caven
"""


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums_numeric = [int(n) for n in nums]
        
        counter = collections.Counter(nums_numeric)
        
        counter_sorted = {key: counter[key] for key in sorted(counter.keys(), reverse = True)}
        
        for key in counter_sorted:
            k -= counter_sorted[key]
            if k <=0:
                return str(key)