# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.lst=[]
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.recurse(root)
        return self.lst
        
    def recurse(self, root):
        if root:
            self.inorderTraversal(root.left)
            self.lst.append(root.val)
            self.inorderTraversal(root.right)
            
        
            
        
        
        
        