# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 15:31:51 2021

@author: Caven
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        elif root.children == []:
            return 1
        else:
            height = [self.maxDepth(x) for x in root.children]
            return max(height) + 1