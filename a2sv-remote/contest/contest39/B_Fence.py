import sys
input = sys.stdin.readline
# from collections import Counter
# import heapq


n, k = [int(a) for a in input().split()]
h = [int(a) for a in input().split()]

minH=sys.maxsize
tot=0
l=0
idx=0
for i in range(n):
    
    tot += h[i]
    if i+1 >= k:
        if tot<minH:
            minH=tot
            idx=i+1
        tot-=h[l]
        l+=1
print(idx-k+1)
