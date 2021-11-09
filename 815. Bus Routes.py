# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 21:17:41 2021

@author: Caven
"""


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: return 0
        
        # You need to record all the buses you can take at each stop so that you can find out all
        # of the stops you can reach when you take one time of bus.
        # the key is stop and the value is all of the buses you can take at this stop.
        stopBoard = collections.defaultdict(list)
        for bus, stops in enumerate(routes):
            for stop in stops:
                stopBoard[stop].append(bus)
        
        # The queue is to record all of the stops you can reach when you take one time of bus.
        queue = deque([source])
        # Using visited to record the buses that have been taken before, because you needn't to take them again.
        visited = set()

        res = 0
        while queue:
            # take one time of bus.
            res += 1
            # In order to traverse all of the stops you can reach for this time, you have to traverse
            # all of the stops you can reach in last time.
            pre_num_stops = len(queue)
            for _ in range(pre_num_stops):
                curStop = queue.popleft()
                # Each stop you can take at least one bus, you need to traverse all of the buses at this stop
                # in order to get all of the stops can be reach at this time.
                for bus in stopBoard[curStop]:
                    # if the bus you have taken before, you needn't take it again.
                    if bus in visited: continue
                    visited.add(bus)
                    for stop in routes[bus]:
                        if stop == target: return res
                        queue.append(stop)
        return -1