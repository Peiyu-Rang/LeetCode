# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 11:39:11 2020

@author: Caven
"""

import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        totalMove = m+n-2
        downMove = m-1
        return int(math.factorial(totalMove)/math.factorial(downMove)/math.factorial(n-1))