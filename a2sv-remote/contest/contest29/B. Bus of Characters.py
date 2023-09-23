import sys
input = sys.stdin.readline
from heapq import heappop, heappush
# from collections import Counter

n= int(input())

w = [int(a) for a in input().split()]

ppl = [int(a) for a in input().strip()]

emptyHeap = []

oneSeat = []
ans = []
for i in range(len(w)):
    heappush(emptyHeap, (w[i], i+1))
for i in ppl:
    if i ==0:
        cur = heappop(emptyHeap)
        ans.append(cur[1])
        heappush(oneSeat, (-1*cur[0], cur[1]))
    else:
        cur = heappop(oneSeat)
        ans.append(cur[1])
print(*ans)