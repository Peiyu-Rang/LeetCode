# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 23:27:16 2021

@author: Caven
"""


from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseDict = defaultdict(list)
        
        for courses in prerequisites:
            nextCourse, prevCourse = courses[0], courses[1]
            courseDict[prevCourse].append(nextCourse)
            
        visited = [False] * numCourses
        visiting = [False] * numCourses
        
        for currCourse in range(numCourses):
            if self.hasCycle(currCourse, courseDict, visited, visiting):
                return False
        return True
    
    def hasCycle(self, currCourse, courseDict, visited, visiting):
        if visited[currCourse]:
            return False
        if visiting[currCourse]:
            return True
        
        visiting[currCourse] = True
        
        res = False
        for nei in courseDict[currCourse]:
            res = self.hasCycle(nei, courseDict, visited, visiting)
            if res: break
        
        visiting[currCourse] = False
        visited[currCourse] = True
        return res
    
    
    
    

class GNode:
    def __init__(self):
        self.inDegrees = 0
        self.outNodes = []

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict, deque
        
        graph = defaultdict(GNode)
        
        totalDeps = 0
        
        for relation in prerequisites:
            nextCourse, prevCourse = relation[0], relation[1]
            graph[prevCourse].outNodes.append(nextCourse)
            graph[nextCourse].inDegrees +=1
            totalDeps +=1
            
        q = deque([])
        
        for key in graph:
            if graph[key].inDegrees == 0:
                q.append(key)
                
        removedEdges = 0
        
        while q:
            course = q.popleft()
            
            for nextCourse in graph[course].outNodes:
                graph[nextCourse].inDegrees -=1
                removedEdges +=1
                
                if graph[nextCourse].inDegrees == 0:
                    q.append(nextCourse)
                    
        
        return removedEdges == totalDeps
    
    
    
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [False] * numCourses
        
        inDegrees = {i:0 for i in range(numCourses)}
        graph = collections.defaultdict(list)
        
        for nextCourse, prevCourse in prerequisites:
            graph[prevCourse].append(nextCourse)
            inDegrees[nextCourse] +=1
        
        q = deque([])
        for course in inDegrees:
            if inDegrees[course] == 0:
                q.append(course)
                
        while q:
            course = q.popleft()
            visited[course] = True
            
            for nextCourse in graph[course]:
                inDegrees[nextCourse] -=1
                if inDegrees[nextCourse] == 0:
                    q.append(nextCourse)
                    
            
        return all(visited)