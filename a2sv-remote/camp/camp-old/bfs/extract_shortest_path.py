
from collections import deque
import sys


def extractShortestPath(parnets, cur):
    shortest_path=[]
    while cur!=(-1,-1):
        shortest_path.append(cur)
        cur=parnets[cur[0]][cur[1]]
    for point in reversed(shortest_path):
        print(point)
    return shortest_path

DIR=[[0,1],[0,-1],[-1,0], [1,0]]

def isValid(mat, visited, row, col):
    N,M=len(mat), len(mat[0])
    
    return (row>=0) and (row<M) and (col>=0)and (col<N) and mat[row][col]==1 and not visited[row][col]

def BFS(mat, i, j, x, y):
    N,M=len(mat), len(mat[0])
    
    visited=[[False for x in range(N)] for y in range(M)]
    parents=[[(-1,-1) for x in range(N)] for y in range(M)]
    
    q= deque([(i, j, 0)])
    visited[i][j]=True
    min_dist=sys.maxsize
    
    while  q:
        (i, j, dist)=q.popleft()
        
        if i==x and j==y:
            min_dist=dist
            return extractShortestPath(parents, (i,j))
        
        for d in DIR:
            if isValid(mat, visited, i+d[0], j+d[2]):
                parents[i+d[0]][j+d[1]]=(i,j)
                visited[i+d[0]][j+d[1]]=True
                q.append((i+d[0], j+d[1], dist+1))
    if min_dist==sys.maxsize:
        return []
    
            
    
    