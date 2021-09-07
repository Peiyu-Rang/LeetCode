# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 22:53:07 2021

@author: Caven
"""


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        res = None
        n = len(releaseTimes)
        for i in range(n):
            if i == 0:
                if res is None:
                    res = (releaseTimes[i], keysPressed[i])
                    continue
            else:
                if releaseTimes[i] - releaseTimes[i-1] > res[0]:
                    res = (releaseTimes[i] - releaseTimes[i-1], keysPressed[i])
                elif releaseTimes[i] - releaseTimes[i-1] == res[0]:
                    if keysPressed[i] > res[1]:
                        res = (releaseTimes[i] - releaseTimes[i-1], keysPressed[i])
                        
        return res[1]