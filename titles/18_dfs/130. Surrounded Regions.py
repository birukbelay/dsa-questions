class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """      
        
        n = len(board)
        m= len(board[0])
        in_bound=lambda row, col:0<=row<n and 0<=col<m
        DIR=[[0,1],[1,0],[-1,0], [0,-1]]

        # 1 capture unsorounded regions (O->T)
        def capture(r,c ):
            if (not in_bound(r,c)) or board[r][c]!="O":
                return
            board[r][c]="T"
            for i,j in DIR:
                capture(r+i, c+j)
        for r in range(n):
            for c in range(m):
                if board[r][c]=='O' and (r in [0, n-1] or c in [0, m-1]):
                    capture(r, c)
        #2. capture the surounded regions
        for r in range(m):
            for c in range(m):
                if board[r][c]=='O':
                    board[r][c]='X'
                elif board[r][c]=='T':
                    board[r][c]="O"



