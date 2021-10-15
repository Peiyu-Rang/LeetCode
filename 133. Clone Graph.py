# -*- coding: utf-8 -*-
"""
Created on Sun May 23 16:06:18 2021

@author: Caven
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.visited = {}
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        if node in self.visited:
            return self.visited[node]
        
        clone_node = Node(node.val, [])
        self.visited[node] = clone_node
        
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]
            
        
        
        return clone_node
    
    
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        q = deque([node])
        visited = {}
        
        visited[node] = Node(node.val, [])
        
        while q:
            curr = q.popleft()
            if curr not in visited:
                visited[curr] = Node(curr.val, [])
                
            for nei in curr.neighbors:
                if nei not in visited:
                    visited[nei] = Node(nei.val, [])
                    q.append(nei)
                    
                visited[curr].neighbors.append(visited[nei])
                
        return visited[node]