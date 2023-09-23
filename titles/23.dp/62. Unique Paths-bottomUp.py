class Solution:
   def uniquePaths(self, m: int, n: int) -> int:
        row ==m-1
        col ==n-1
        state =[ [0] *n for _ in range(m)]
        state[m][n]=1

        def getVal(r, c):
            if r<m and c<n:
                return state[r][c]
            else:
                return 0
        
        for i in range(m, -1,-1):
            for j in range(n, -1, -1):
                right = getVal(i, j+1)
                down = getVal(i+1, j)
                state[i][j]=right + down
        return state[0][0]
