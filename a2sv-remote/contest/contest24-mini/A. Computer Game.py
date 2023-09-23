import sys
input = sys.stdin.readline
from collections import deque



def soln(arr, le):
    DIR= [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)  ]
    n,m=2, le
    in_bound= lambda row, col: 0<=row <n and 0<=col<m
    que= deque()
    que.append((0,0))
    arr[0][0]=2
    # print("arr-",arr)
    while que:
        cur = que.popleft()
        
        if (cur[0], cur[1]) == (1, m-1):
            return True

        for i,j in DIR:
            px=cur[0] +i
            py=cur[1] +j
            
            if in_bound(px, py) and arr[px][py]==0:
                
                arr[px][py]=2
                que.append((px, py))
    return False

# print(soln([[0,0,1,1], [1,1,0,0]],4))

t= int(input())
for i in range(t):

    n= int(input())
    
    i1=input().strip()
    

    i2=input().strip()
    
    arr1 = [int(a) for a in i1]
    arr2 = [int(a) for a in i2]
    

    if soln([arr1, arr2], n):
        print("YES")
    else:
        print("NO")