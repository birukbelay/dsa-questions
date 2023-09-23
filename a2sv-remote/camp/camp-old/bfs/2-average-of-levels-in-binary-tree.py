# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.dict_sum={}
        self.dict_count={}        
        
    def bfs(self, root, level):
        if root==None:
            return
        if (level+1) in self.dict_sum:
            self.dict_sum[level+1]+=root.val
        else:
            self.dict_sum[level+1]=root.val
        if (level+1) in self.dict_count:
            self.dict_count[level+1]+=1
        else:
            self.dict_count[level+1]=1
        
        if root.left!=None:            
            self.bfs(root.left, level+1)        
        if root.right!=None:            
            self.bfs(root.right, level+1)
        
        
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        self.bfs(root, 0)
        arr=[]
        
        
            
        print(self.dict_sum)
        for key in self.dict_sum:
            arr.append(self.dict_sum[key]/self.dict_count[key])
        return arr