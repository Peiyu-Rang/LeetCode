# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 22:39:28 2020

@author: Caven
"""

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right= n
        while (left < right):
            mid = left + (right - left)//2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid+1
        
        return left