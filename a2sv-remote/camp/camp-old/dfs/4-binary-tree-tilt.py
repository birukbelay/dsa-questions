# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def __init__(self):
        self.tot_sum = 0
    def dfs(self, root):
        if root==None:
            return 0      

        leftSum=0
        rightSum=0
        if root.left!=None :
            leftSum=self.dfs(root.left)
        if root.right!=None:
            rightSum=self.dfs(root.right)
        sums=abs(leftSum-rightSum)        
        self.tot_sum+=sums
        return root.val + leftSum + rightSum
            
    
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.tot_sum
        
  