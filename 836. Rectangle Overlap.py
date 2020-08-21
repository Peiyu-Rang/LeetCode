# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 07:40:54 2020

@author: Caven
"""

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # if any of the corner of one rectangle is in antoher, they overlap
        

        return not (rec1[2] <= rec2[0] or #left
                    rec1[3] <= rec2[1] or #down
                    rec1[0] >= rec2[2] or #right
                    rec1[1] >= rec2[3]) #top
                