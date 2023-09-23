"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self):
        self.depth = 0
        
    def dfs(self, root: 'Node', length) -> int:
        
        # print(length)
        if root==None:            
            # self.depth= max(pathLen, self.depth)
            return
        pathLen= length+1
        for child in root.children:
            self.dfs(child,pathLen)
        self.depth= max(pathLen, self.depth)
            
    def maxDepth(self, root: 'Node') -> int:        
        self.dfs(root, 0)        
        return self.depth