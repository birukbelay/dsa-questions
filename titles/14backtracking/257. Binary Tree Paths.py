# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        self.allPath=[]
        
        def go(node, path):
            path.append(str(node.val))
            if not node.left and not node.right:
                cur= '->'.join(path)
                self.allPath.append(cur)
                return
            if node.left:
                go(node.left, path[:])
            if node.right:
                go(node.right, path[:])
        
        go(root,[])
        return self.allPath
                
            
        
        