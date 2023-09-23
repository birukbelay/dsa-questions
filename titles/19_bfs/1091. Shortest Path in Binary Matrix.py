class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        n,m=len(grid), len(grid[0])
        DIR= [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)  ]
        
        
        que= deque()
        
        in_bound= lambda row, col: 0<=row <n and 0<=col<m
        if grid[0][0]==1 or grid[n-1][m-1]==1:
            return -1
        que.append((0,0, 1))
        maxDis=0
        while que:
            cur= que.popleft()
            if (cur[0],cur[1])==(n-1, m-1):
                return cur[2]
            maxDis= max(maxDis, cur[2])
            for i,j in DIR:
                px=cur[0] +i
                py=cur[1] +j
                
                
                if in_bound(px, py) and grid[px][py]==0:
                    grid[px][py]=2
                    que.append((px, py, cur[2]+1))
        return -1
                    
                
        
        