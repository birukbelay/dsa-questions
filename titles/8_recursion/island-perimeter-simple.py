class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        seen = set()
        # directions = ((-1, 0), (0, -1), (1, 0), (0, 1))

        def in_bound(row, col):
            return 0 <= row < n and 0 <= col < m

        def dfs(row, col):
            if (row, col) in seen:
                return 0
            if not in_bound(row, col) or grid[nrow][ncol] == 0:
                return 1
            seen.add((row, col))
            
            perim=dfs(row, col+1)           
            perim+=dfs(row, col+-1)           
            perim+=dfs(row+1, col)           
            perim+=dfs(row-1, col)           
            
            return perim
        
        # find one cell which is island
        for row in range(n):
            for col in range(m):
                # Find an island & is not in seen
                if grid[row][col] == 1 and (row, col) not in seen:
                    seen.add((row, col))
                    return dfs(row, col)
        

        
 
