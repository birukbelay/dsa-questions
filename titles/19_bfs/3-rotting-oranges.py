from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        n,m= len(grid), len(grid[0])
        in_bound=lambda row, col:0<=row<n and 0<=col<m
        DIR=[[0,1],[1,0],[-1,0], [0,-1]]
        
        # visited=set()
#         help us iterate the grids in order

        minuteCtr=0
        
        rottenQueue=deque()
        # freshQueue=deque()
        freshCtr=0
    
        #         finding all the rotten and fresh tomatoes
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    rottenQueue.append((i,j,0))
                elif grid[i][j]==1:
                    freshCtr+=1                                        

        while rottenQueue:
            cur=rottenQueue.popleft()
            for i, j in DIR:
                ptx=cur[0] + i
                pty=cur[1] +j
                # minute=current[2]
                
                minuteCtr=max(cur[2], minuteCtr)
                
                if in_bound(cur[0]+i, cur[1]+j) and grid[ptx][pty]==1:
                    grid[ptx][pty]=2 #to mark the visited cells so no need for visited set
                    rottenQueue.append((ptx,pty,cur[2]+1))
                    # print( minute)
                    
                    print(freshCtr)
                    freshCtr-=1
        if freshCtr>0:
            print(freshCtr)
            return -1
        else:
            print("min",minuteCtr)
            return minuteCtr