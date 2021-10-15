# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 21:41:39 2021

@author: Caven
"""


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        if n == 0:
            return 0
        for i in range(1, n):
            costs[i][0] += min(costs[i-1][1] , costs[i-1][2])
            costs[i][1] += min(costs[i-1][0] , costs[i-1][2])
            costs[i][2] += min(costs[i-1][1] , costs[i-1][0])

        return min(costs[n-1])
        