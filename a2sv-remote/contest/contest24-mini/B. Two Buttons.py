import sys
input = sys.stdin.readline
from collections import deque

n, m = [int(a) for a in input().split() ]

def find(n, m):
    #9999 10000
    #4 6
    
    # diff1= n*2 -m
    # diff2 = n- m//2
    ctr=0
    que= deque()
    
    
    visited= set()
    que.append(n)
    
    
    while que:
        for i in range(len(que)):
            
            cur= que.popleft()
            if cur==m:
                return ctr
            
            
            if cur-1 not in visited or cur-1 !=0:
                que.append(cur-1)
                visited.add(cur)
            if cur<m:
                if cur *2 not in visited:
                    que.append(cur*2)
                    visited.add(cur*2)
                
        ctr+=1
    return ctr
print(find(n,m))
        
