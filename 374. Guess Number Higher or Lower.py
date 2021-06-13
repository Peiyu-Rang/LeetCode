# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 16:38:00 2021

@author: Caven
"""


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        
        mid = (left + right) // 2
        
        while left <= right:
            if guess(mid) == 0:
                return mid
            elif guess(mid) < 0:
                right = mid-1
            else:
                left = mid+1

            mid = (left + right) // 2