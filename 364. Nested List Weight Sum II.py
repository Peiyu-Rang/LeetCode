# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 22:10:27 2021

@author: Caven
"""


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        max_depth = self.depth(nestedList)
        self.res = 0
        self.visit(nestedList, max_depth, 1)
        
        return self.res
        
    
    
    def depth(self, nestedList):
        curr_depth = 1
        for x in nestedList:
            if not x.isInteger():
                curr_depth = max(curr_depth, 1+self.depth(x.getList()))
        
        return curr_depth
    
    def visit(self, nestedList, max_depth, level):
        for x in nestedList:
            if x.isInteger():
                self.res += x.getInteger()*(max_depth-level+1)
            else:
                self.visit(x.getList(), max_depth, level + 1)
                
        return
    