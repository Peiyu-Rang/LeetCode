# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 18:18:23 2021

@author: Caven
"""

"""
dp[i] = Min cost at day i to fill the travel plan
dp[i] = min(costs[0] + dp[i+1], costs[1] + dp[i+7], costs[2] + dp[i+30])
"""

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * 396
        for i in range(len(days)-1, -1, -1):
            op0 = costs[0] + dp[days[i]+1]
            op1 = costs[1] + dp[days[i]+7]
            op2 = costs[2] + dp[days[i]+30]
            dp[days[i]] = min([op0, op1, op2])
            if i > 0:
                for j in range(days[i], days[i-1], -1):
                    dp[j] = dp[days[i]]

        return dp[days[0]]