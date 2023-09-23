# https://leetcode.com/problems/symmetric-tree/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:    
    def dfsleft(self, root, q):
        if root==None:
            return
        root.val=None
        
        if root.left!=None:
            q.append(root.left.val)
            self.dfsleft(root.left, q)
        else:
            q.append(None)
        if root.right!=None:
            q.append(root.right.val)
            self.dfsleft(root.right, q)
        else:
            q.append(None)
    def dfsRight(self, root, q):
        if root==None:
            return
        # q.append(root.val)
        if root.right!=None:
            q.append(root.right.val)
            self.dfsRight(root.right, q)
        else:
            q.append(None)
        if root.left!=None:
            q.append(root.left.val)
            self.dfsRight(root.left, q)
        else:
            q.append(None)
        
    
        
    def isSymmetric(self, root: TreeNode) -> bool:
        arr1=[]
        arr2=[]
        if root.left!=None:            
            arr1.append(root.left.val)
        if root.right!=None:            
            arr2.append(root.right.val)
        
            
        self.dfsleft(root.left, arr1)        
        self.dfsRight(root.right, arr2)
        
        print("arr1=", arr1)
        print("arr2=", arr2)
        if arr1==arr2:
            return True
        else:
            return False
        
    
        

        
        
        