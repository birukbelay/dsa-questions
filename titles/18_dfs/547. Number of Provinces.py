class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n, m = len(isConnected), len(isConnected[0])
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        def in_bound(row, col):
            return 0 <= row < n and 0 <= col < m
        
        seen = set()
        ctr=0
        def dfs(i, j):
            
            
            for x, y in dirs:
                nr = i + x
                nc = j + y
                
                if in_bound(nr, nc) and isConnected[nr][nc]==1 and (nr, nc) not in seen:
                    dfs(nr, nc)
        for row in range(n):
            for col in range(m):
                if isConnected[row][col] ==1 and (row, col) not in seen:
                    seen.add((row, col))
                    ctr+=1
                    dfs(row, col)
        return ctr
                    
                    
                
            
        
        
        
        