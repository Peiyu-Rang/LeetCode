# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
        if not root:
            return root
        
        seen = {}
        stack = [root]
            
        while stack:
            node = stack.pop()
            if node not in seen:
                seen[node] = NodeCopy(node.val, None, None, None)
            
            if node.left:
                if node.left not in seen:
                    seen[node.left] = NodeCopy(node.left.val, None, None, None)
                seen[node].left = seen[node.left]
                stack.append(node.left)
            
            if node.right:
                if node.right not in seen:
                    seen[node.right] = NodeCopy(node.right.val, None, None, None)
                seen[node].right = seen[node.right]
                stack.append(node.right)
                
            if node.random:
                if node.random not in seen:
                    seen[node.random] = NodeCopy(node.random.val, None, None, None)
                seen[node].random = seen[node.random]
                
            
        return seen[root]
        