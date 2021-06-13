# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 16:10:40 2021

@author: Caven
"""


class Building:
    def __init__(self, values):
        self.l = values[0]
        self.r = values[1]
        self.h = values[2]
        
    def __lt__(self, other):
        return self.h > other.h
        
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        buildings = [Building(values) for values in buildings]
        heap, res = [], []
        index, n = 0, len(buildings)
        curSkyline = 0
        events = set()
        for building in buildings:
            events.add(building.l)
            events.add(building.r)
        events = list(events)
        events.sort()
                
        def popExpiredBuildings(x):
            while heap:
                if heap[0].l <= x < heap[0].r:
                    break
                heappop(heap)
                
        for ev in events:
            while 0 <= index < n and buildings[index].l <= ev <= buildings[index].r:
                heappush(heap, buildings[index])
                index += 1
            
            popExpiredBuildings(ev)
            if heap and curSkyline != heap[0].h:
                curSkyline = heap[0].h
                res.append([ev, curSkyline])
            elif not heap and curSkyline != 0:
                res.append([ev, 0])
                curSkyline == 0
                
        return res