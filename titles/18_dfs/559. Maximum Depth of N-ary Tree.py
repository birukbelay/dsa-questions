# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
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
        
        
        if root==None:           
            return
        pathLen= length+1
        for child in root.children:
            self.dfs(child, pathLen)
        self.depth= max(pathLen, self.depth)
            
    def maxDepth(self, root: 'Node') -> int:        
        self.dfs(root, 0)        
        return self.depth
    
        