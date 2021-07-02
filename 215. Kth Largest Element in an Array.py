# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 22:33:54 2021

@author: Caven
"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        counter_sort = {k:v for k, v in sorted(counter.items(), key = lambda item: item[0], reverse = True)}
        
        for i, key in enumerate(counter_sort):
            k -= counter_sort[key]
            if k <= 0:
                return key
            else:
                continue