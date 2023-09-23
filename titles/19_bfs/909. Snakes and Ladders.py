from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        DIR=[(0,1),(0,-1), (1, 0)]

        row = len(board)
        col= len(board[0])
        board.reverse()
        def intToPos(square):
            r=(square-1)//row
            c=(square-1)%row
            if r%2:
                c= row-1-c
            return [r,c]
        
        q= deque() # [square, moves]
        q.append([1,0])
        seen=set()
        while q:
            square, moves = q.popleft()

            for i in range(1,7):
                nxtSq = square +i
                r,c = intToPos(nxtSq)
                if board[r][c] !=-1:
                    nxtSq=board[r][c]
                if nxtSq == len(board)**2:
                    return moves +1
                if nxtSq not in seen:
                    seen.add(nxtSq)
                    q.append([nxtSq, moves+1])
        return -1