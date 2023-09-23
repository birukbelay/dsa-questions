from collections import deque

DIR=[[0,1],[1,0],[-1,0], [0,-1]]
def inBound(list, index):
    if index>=len(list):
        return False
    return True

def shortest(start, matrix, x,y):
    n,m=len(matrix), len(matrix[0])
    in_bound= lambda row, col:0<=row< n and 0<=col<m
    
    visited=set()
    queue=deque([(start[0],start[1], 0)])
    counter=0
    # make the first cell visited
    visited.add((0,1, 0))
    while queue:
        current=queue.popleft()
        
        for i in DIR:
            ptx=current[0] + i[0]
            pty=current[1]+i[1]
            distance=current[2]
            if (matrix[ptx][pty])==(x,y):
                    return distance+1
            
            if in_bound(ptx, pty) and (ptx, pty) not in visited and matrix[ptx][pty]==1:   
                
                visited.add(ptx, pty, distance+1)                
                queue.append((ptx, pty, distance+1))
    return(-1,-1) 
                
                
                
        
                
            
            
        
    
    