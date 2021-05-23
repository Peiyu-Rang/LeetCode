# -*- coding: utf-8 -*-
"""
Created on Thu May 20 21:54:48 2021

@author: Caven
"""


class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = [i * i for i in range(1, int(n**0.5)+1)]
        
        level = 0
        queue = {n}
        
        while queue:
            level +=1
            
            next_queue = set()
            
            for remainder in queue:
                for sq in square_nums:
                    if remainder == sq:
                        return level
                    elif remainder < sq:
                        break
                    else:
                        next_queue.add(remainder - sq)
                        
            queue = next_queue
            
        return level
        