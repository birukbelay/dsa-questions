# https://www.eolymp.com/en/contests/9060/problems/78602
import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
k = int(input())
d= defaultdict(list)

for  i in range(k):
    arr = [int(a) for a in input().split()]
    if arr[0]==1:
        j, l = arr[1], arr[2]
        d[j].append(l)
        d[l].append(j)
    elif arr[0]==2:
        print(*d[arr[1]])
    

