import sys
input = sys.stdin.readline
# from collections import Counter


r,c = [int(a) for a in input().split()]
arr= []
for i in range(r):
    s = input().strip()
    arr.append(s)


DIR = [(1, 0), (-1, 0), (0, -1),  (0, 1)]
in_bound = lambda row, col: 0 <= row < r and 0 <= col < c


d={}
def dfs(i,j, visited, ci, cj):
    if not in_bound(i,j):
        return 0
    if (i,j) in visited:
        return 0
    visited.add((i,j))
    if (i,j)!=(ci, cj) and arr[i][j]=='*':
        return 0

    tot= 0
    for row,col in DIR:
        cnt = dfs(i+row, j+col, visited, ci, cj)
        tot+=cnt
    
    # d[(i,j)]=tot+1
    return tot+1
ans = [[0]*c for _ in range(r)]
for i in range(r):
    for j in range(c):
        visited = set()
        if arr[i][j]=='.':
            ans[i][j]='.'
            continue
        val= dfs(i, j, visited, i, j)
        ans[i][j]=str(val)


# print(ans)
for st in ans:
    s =''.join(st)
    print(s)







# def find(i, j):
#     if not in_bound(i,j):
#         return 0
#     if arr[i][j]=='*':
#         return 1
#     fin = d[(i,j)]
#     return fin-1 if fin>0 else 0
# ans = [[0]*c for _ in range(r)]

# for i in range(r):
#     for j in range(c):
        
#         if arr[i][j]=='.':
#             ans[i][j]='.'
#             continue
#         tot=0
#         for row,col in DIR:
#             cnt = find(i+row, j+col)
#             tot+=cnt
#         ans[i][j]=str(tot)