# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 16:56:46 2021

@author: Caven
"""


class Solution:

    def __init__(self, w: List[int]):
        total = sum(w)
        self.cdf = []
        curr_sum = 0
        for weight in w:
            curr_sum += weight / total
            self.cdf.append(curr_sum)

    def pickIndex(self) -> int:
        p = random.random()
        return self.binarySearch(p)
    
    def binarySearch(self, p):
        left = 0
        right = len(self.cdf) -1
        while left < right:
            mid = (left + right) // 2
            if self.cdf[mid] >= p and (self.cdf[mid-1] < p or mid ==0):
                return mid
            elif self.cdf[mid] < p:
                left = mid +1
            else:
                right = mid - 1
                
        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()