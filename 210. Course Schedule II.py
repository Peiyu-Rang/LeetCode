# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 17:50:13 2021

@author: Caven
"""


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)
        res = []
        took = set()
        
        for course, pre in prerequisites:
            graph[course].add(pre)
            
        q = deque()
        for key in range(numCourses):
            if len(graph[key]) == 0:
                q.append(key)
                
        while q:
            course = q.popleft()
            
            if course in took:
                continue

            res.append(course)
            took.add(course)

            for key in graph:
                if course in graph[key]:
                    graph[key].remove(course)
                    if len(graph[key]) == 0:
                        q.append(key)
                        
        return res if len(res) == numCourses else []