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