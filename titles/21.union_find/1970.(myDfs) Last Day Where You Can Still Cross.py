class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:

        matrix = [[0]*col for _ in range(row)]
        curday=0
        DIR= [(0, 1), (0, -1), (-1,0), (1, 0)]
        def in_bound(r,c):
            return 0<= r<row and 0 <= c < col
        
        def find(r, c, seen):
            if (r,c) in seen or not in_bound(r,c):
                return False
            if r==0:
                return True
            seen.add((r,c))
            for m,n in DIR:
                if find(r+m, c+n, seen):
                    return True
            return False


        def check():

            for c in range(col):
                cell = matrix[-1][c]
                if cell==0:
                    ans = find(row-1, c, set())
                    if ans:
                        return True
            return False
        for i,j in cells:
            matrix[i-1][j-1]=1

            ans =check()
            if ans:
                curday +=1
            else:
                return curday
        return curday