# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], lower=-sys.maxsize, upper=sys.maxsize) -> bool:
        
         
        if not root:
            return True
        if root.val<=lower or root.val>=upper:
            return False
        
#         if root.left:
#             if root.left.val>= root.val:
#                 return False            
#         if root.right:
#             if root.right.val<=root.val:               
#                 return False
            
            
        return self.isValidBST(root.left, lower, root.val) and self.isValidBST(root.right, root.val, upper)
        
        
             
    
    