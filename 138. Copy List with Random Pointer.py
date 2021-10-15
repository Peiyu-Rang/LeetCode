# -*- coding: utf-8 -*-
"""
Created on Thu May 13 20:59:18 2021

@author: Caven
"""


class Solution(object):
    def __init__(self):
        # Creating a visited dictionary to hold old node reference as "key" and new node reference as the "value"
        self.visited = {}

    def getClonedNode(self, node):
        # If node exists then
        if node:
            # Check if its in the visited dictionary          
            if node in self.visited:
                # If its in the visited dictionary then return the new node reference from the dictionary
                return self.visited[node]
            else:
                # Otherwise create a new node, save the reference in the visited dictionary and return it.
                self.visited[node] = Node(node.val, None, None)
                return self.visited[node]
        return None

    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        if not head:
            return head

        old_node = head
        # Creating the new head node.       
        new_node = Node(old_node.val, None, None)
        self.visited[old_node] = new_node

        # Iterate on the linked list until all nodes are cloned.
        while old_node != None:

            # Get the clones of the nodes referenced by random and next pointers.
            new_node.random = self.getClonedNode(old_node.random)
            new_node.next = self.getClonedNode(old_node.next)

            # Move one step ahead in the linked list.
            old_node = old_node.next
            new_node = new_node.next

        return self.visited[head]
    
    
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        
        seen = {}
        stack = [head]
        
        while stack:
            node = stack.pop()
            if node not in seen:
                seen[node] = Node(node.val)
            
            if node.next:
                if node.next not in seen:
                    seen[node.next] = Node(node.next.val)
                
                seen[node].next = seen[node.next]
                stack.append(node.next)
                
            if node.random:
                if node.random not in seen:
                    seen[node.random] = Node(node.random.val)
                
                seen[node].random = seen[node.random]
                
        return seen[head]
    
    
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        
        pt = head
        
        while pt:
            new_node = Node(pt.val)
            new_node.next = pt.next
            pt.next = new_node
            pt = new_node.next
            
        pt = head
        while pt:
            pt.next.random = pt.random.next if pt.random else None
            pt = pt.next.next
            
        pt_old = head
        pt_new = head.next
        
        head_new = head.next
        
        while pt_old:
            pt_old.next = pt_old.next.next
            pt_new.next = pt_new.next.next if pt_new.next else None
            pt_old = pt_old.next
            pt_new = pt_new.next
            
        return head_new