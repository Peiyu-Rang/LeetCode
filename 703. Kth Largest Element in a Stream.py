# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 08:05:15 2020

@author: Caven
"""
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pool = nums
        heapq.heapify(self.pool)
        self.k = k
        while(self.pool is not None and len(self.pool) > k):
            heapq.heappop(self.pool)

    def add(self, val: int) -> int:
        if len(self.pool) < self.k:
            heapq.heappush(self.pool,val)
        elif val > self.pool[0]:
            heapq.heappushpop(self.pool,val)
            
        return self.pool[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)