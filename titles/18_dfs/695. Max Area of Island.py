class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        n, m = len(grid), len(grid[0])
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        
        def in_bound(row, col):
            return 0 <= row < n and 0 <= col < m
        
        seen = set()
        
        maxT= 0
        def dfs(i, j, cnt):
            seen.add((i, j))
            
            ct=0
            
            for x, y in dirs:
                nr = i + x
                nc = j + y
                
                if in_bound(nr, nc) and grid[nr][nc]==1 and (nr, nc) not in seen:
                    ct+=1
                    ct+= dfs(nr, nc, cnt+1)
            return ct
                    
        for row in range(n):
            for col in range(m):
                if grid[row][col] ==1 and (row, col) not in seen:
                    
                    tot = dfs(row, col, 1)
                    maxT= max(maxT, tot+1)
        return maxT