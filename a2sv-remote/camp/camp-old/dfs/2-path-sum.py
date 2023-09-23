# https://leetcode.com/problems/path-sum/submissions/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        self.isTrue=False
        
        self.dfs(root, targetSum, 0)
        return self.isTrue
        
    def dfs(self, root, targetSum, totalSum):
        if root==None:
            return
        sum = totalSum + root.val
        
        if root.left==None and root.right ==None:
            if sum==targetSum:
                self.isTrue=True
                return True
            else:
                return
                       
        if root.left!=None :
            self.dfs(root.left, targetSum, sum)
        if root.right!=None:
            self.dfs(root.right, targetSum, sum)