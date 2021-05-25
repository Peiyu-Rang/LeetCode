# -*- coding: utf-8 -*-
"""
Created on Mon May 24 20:34:01 2021

@author: Caven
"""


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = [False] * len(rooms)
        seen[0] = True
        stack = [0]
        
        while stack:
            curr = stack.pop()
            for nei in rooms[curr]:
                if not seen[nei]:
                    seen[nei] = True
                    stack.append(nei)
                    
        return all(seen)