# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 23:10:17 2021

@author: Caven
"""


class Solution:

    def __init__(self, nums: List[int]):
        self.origin = list(nums)
        self.n = len(nums)
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.origin
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        i = 0
        while i < self.n:
            rand_idx = random.randrange(i, self.n)
            self.nums[i], self.nums[rand_idx] = self.nums[rand_idx], self.nums[i]
            i+=1
        return self.nums
            


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()