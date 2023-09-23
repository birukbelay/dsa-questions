import sys
input = sys.stdin.readline
# from collections import Counter

arr = [int(a) for a in input().split()]

r1 = arr[0]
c1=arr[1]
r2, c2 = arr[2], arr[3]


rook=0
bishop=0
king=0
# bishops move
if abs(r1-r2)==abs(c1-c2):
    bishop= 1
elif (r1+c1)%2 == (r2+c2)%2:
    bishop =2
else:
    bishop = 0
# rooks move
if r1==r2 or c1==c2:
    rook=1
else:
    rook=2



def in_bound(row, col):
    return 1 <= row < 9 and 1 <= col < 9
DIR = [(1, 0), (-1, 0), (0, -1),  (0, 1), (-1,-1),(1, -1), (1, 1),(-1,1)]
visited=set()
def dfs(r,c, dis, minDis):
    
    if not in_bound(r,c):
        return 9
    if (r,c)==(r2,c2):        
        return dis
    if (r,c ) in visited:
        return 9
    visited.add((r,c))
    for i,j in DIR:
        ans= dfs(r+i, c+j, dis+1, minDis)
        minDis= min(minDis, ans)
    return minDis 
minDis=dfs(r1, c1,0,9)

print(rook, bishop, minDis)





