# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 15:46:57 2021

@author: Caven
"""


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        size = len(flowerbed)
        count = 0
        i = 0
        
        while i < size:
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == size-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                count +=1
                if count >= n:
                    return True
                
            i +=1
            
        return count >= n