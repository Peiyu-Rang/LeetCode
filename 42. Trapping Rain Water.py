# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 21:20:52 2020

@author: Caven
"""
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        if height is None:
            return 0
        n = len(height)
        if n == 0:
            return 0
        left_max = [0] * n
        right_max = [0] * n
        
        left_max[0] = height[0]
        for i in range(1,n):
            left_max[i] = max(height[i], left_max[i-1])
        
        right_max[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right_max[i] = max(height[i], right_max[i+1])
            
        ans = 0
        for i in range(1,n):
            ans += min(left_max[i], right_max[i]) -height[i]
        
        return ans
        
        
if __name__ == '__main__':
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    sol = Solution()
    res = sol.trap(height)
    print(res)
    