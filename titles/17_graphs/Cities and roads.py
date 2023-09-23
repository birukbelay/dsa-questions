import sys
input = sys.stdin.readline


n = int(input())
mat=[]
for i in range(n):
    arr= [int(a) for a in input().split()]
    mat.append(arr)
visited=set()
for i in range(len(mat)):
    for j in range(len(mat[0])):

        if mat[i][j]==1:
            visited.add((max(i,j), min(i,j)))
print(len(visited))