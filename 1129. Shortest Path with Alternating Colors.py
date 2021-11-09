# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 22:08:45 2021

@author: Caven
"""


class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        graph = {1:collections.defaultdict(list), -1:collections.defaultdict(list)}
        
        for u, v in red_edges:
            graph[1][u].append(v)
        
        for u, v in blue_edges:
            graph[-1][u].append(v)
        
        
        res = [float('inf')] * n
        q = deque([(0,-1), (0,1)])
        level = -1
        while q:
            level += 1
            size = len(q)
            for i in range(size):
                node, color = q.popleft()
                opp_color = color * -1
                res[node] = min(level, res[node])
                neighbors = graph[opp_color][node]
                for child in list(neighbors):
                    graph[opp_color][node].remove(child)
                    q.append((child, opp_color))
        return [r if r != math.inf else -1 for r in res]
        
            