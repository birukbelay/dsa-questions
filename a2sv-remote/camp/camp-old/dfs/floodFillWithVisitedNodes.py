
from re import M


def in_bound(list, index):
    if index>=len(list):
        return False
    return True

class Solution:   
    def inBound(self, list, index):
        if index>=len(list) and index<0:
            return False
        return True
        
    def floodFill(self, image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:
        print(0)
        visited=set()
        self.dir=(1,0,-1,0,1)
        removedColor=image[sr][sc]
    
    
    
    # def dfs(self, image, sr, sc, newColor, target):
    def dfs(image, row, col):
        image[row][col]= newColor
        
        for direction in DIR:
            new_row, new_col =row+direction[0], col+direction[1]
            
            if not in_bound(new_row, new_col) or image[new_row, new_col]!=start
        
# def floodFill(image: list[list[int]], sr:int, sc:int, newColor:int)->list[list[int]]:
#     dfs(image, sr, sc)
#     return image
    
    
    
DIR=[[0,1],[1,0],[-1,0], [0,-1]]



    
    