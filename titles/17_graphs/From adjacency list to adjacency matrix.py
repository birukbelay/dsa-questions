# https://www.eolymp.com/en/contests/9060/problems/78604

import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())

# d= defaultdict(list)
mat = [[0 for a in range(n)] for _ in range(n) ]
for  i in range(n):
    arr = [int(a) for a in input().split()]
    # print(i,"--",arr)
    if arr[0]>0:
        for j in range(1, len(arr)):
            # print(j,"j",arr[j])
            mat[i][arr[j]-1]=1
for i in mat:
    print(*i)
