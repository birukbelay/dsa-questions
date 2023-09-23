# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/submissions/
def inBound(list, index):
    if index>=len(list):
        return False
    return True


class Solution:
    
    def dfs(self, image, sr, sc, newColor, target):    
            image[sr][sc]=newColor             
        
            if inBound(image[sr], sc+1) and image[sr][sc+1]==target:
                self.dfs(image, sr, sc+1, newColor, target)
            if sc> 0 and image[sr][sc-1] ==target:
                self.dfs(image, sr, sc-1, newColor, target)
            if inBound(image, sr+1) and image[sr+1][sc]==target:
                self.dfs(image, sr+1, sc, newColor, target)
            if sr>0 and image[sr-1][sc]==target:
                self.dfs(image, sr-1, sc, newColor, target)
            else:
                return 
    
    def floodFill(self, image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:
        
        if  image[sr][sc]==newColor:
            return image
        self.dfs(image, sr, sc, newColor, image[sr][sc])
        return image