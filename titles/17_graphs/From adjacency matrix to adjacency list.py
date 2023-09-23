
import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())

d= defaultdict(list)
mat= []
for i in range(n):
    arr= [int(a) for a in input().split()]
    mat.append(arr)
for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j]==1 and i!=j:
            d[i].append(j+1)
            

# print(d)
for i in range(n):
    print(len(d[i]), *d[i])