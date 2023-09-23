import sys
input = sys.stdin.readline().strip()
from collections import deque

# n= int(input())

# n, m = [int(a) for a in input().split()]

DIR =[(1,0),(-1, 0), (0, 1),(0, -1)]
def findVol(n,m, grid):

    in_bound = lambda x,y : 0<=x<n and 0<=y<m
    seen = set()


    maxVol=0

    for i in range(n):
        for j in range(m):

            if (i,j) not in seen:
                que= deque()
                # seen.add((i,j))
                que.append((i,j))
                tot=0
                while que:
                    cur=que.popleft()
                    seen.add((cur[0], cur[1]))
                    tot+=grid[cur[0]][cur[1]]
                    for row,col in DIR:
                        ptx=cur[0] + row
                        pty=cur[1] +col
                        if in_bound(ptx, pty) and grid[ptx][pty]!=0:
                            grid[ptx][pty]=0
                            que.append((ptx, pty))
                maxVol= max(maxVol, tot)
    return maxVol
                            
g=[[1, 2, 0],
[3, 4, 0],
[0, 0, 5]]
print(findVol(3, 3, g))

