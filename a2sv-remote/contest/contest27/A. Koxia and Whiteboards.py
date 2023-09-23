import sys
input = sys.stdin.readline
import heapq
# from collections import heapq

n= int(input())

for _ in range(n):
    heap1=[]
    heap2=[]
    n,m = [int(a) for a in input().split()]
    for a in input().split():
        heapq.heappush(heap1, -int(a))
    for b in input().split():
        heapq.heappush(heap2, -int(b))
    sum=0
    if n>=m:
        for i in range(m):
            sum+= heapq.heappop(heap2) *-1
        for i in range(n-m):
            sum+= heapq.heappop(heap1) *-1
    else:
        for i in range(n):
            sum+= heapq.heappop(heap2) *-1
    print(sum)

