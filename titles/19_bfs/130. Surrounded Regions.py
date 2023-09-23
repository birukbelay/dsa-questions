class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        
        n = len(board)
        m= len(board[0])
        in_bound=lambda row, col:0<=row<n and 0<=col<m
        DIR=[[0,1],[1,0],[-1,0], [0,-1]]
        
        
        
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
        for r in range(n):
            for c in range(m):
                if board[r][c]=='O':
                    board[r][c]='X'
                elif board[r][c]=='T':
                    board[r][c]="O"
        
        
        
        
        
        
        
#         my first soln that didnt work
        
        """
        
        
      
        visited=set()
        def explore(i,j):
            if not in_bound(i,j):
                return False
            
            if board[i][j]=='X':
                return True
            
            for x,y in DIR:
                px = 
        def dfs(i,j, sym, isX):
            if not in_bound(i,j):
                return False
            
            if board[i][j]=='X':
                return True
            # print(i,j, sym, isX)
            if isX=='x':
                return dfs(i+ sym, j, sym, isX)
            else:
                return dfs(i, j+sym, sym, isX)
            
            
            
            return
        
        for i in range(n):
            for j in range(m):
                if board[i][j] =="O":
                    
                    l= dfs(i-1, j, -1, 'x')#go up
                    r= dfs(i+1, j,  1, 'x')#go down
                    t= dfs(i, j-1, -1, 'y')#go left
                    b= dfs(i, j+1,  1, 'y')#go right
                    # print("--", i,j,"l-", l, "r-",r, "t-",t,"b-",b)
                    if l and r and t and b:
                        print("----",i,j)
                        board[i][j]="X"
                    
                    
    """              
                    
                