# https://leetcode.com/problems/recover-binary-search-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        arr=[]
        
        def dfs(root):
            
            if root.left:
                dfs(root.left)
            arr.append(root.val)
            if root.right:
                dfs(root.right)
        dfs(root)
        newArr=sorted(arr)
        diff=[]
        for i in range(len(arr)):
            if arr[i]!=newArr[i]:
                diff.append(arr[i])
        def discover(root, a, b):
            if root.val==a:
                root.val=b
            elif root.val==b:
                root.val=a
            if root.left:
                discover(root.left, a,b)
            if root.right:
                discover(root.right, a, b)
        discover(root, diff[0], diff[1])
        # print(diff)