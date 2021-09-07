# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 23:03:36 2021

@author: Caven
"""


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key = lambda x: x[1], reverse = True)
        
        res = 0
        for box, units in boxTypes:
            if truckSize >= box:
                res += box * units
                truckSize -= box
            else:
                res += truckSize * units
                break
        return res
                
        
        