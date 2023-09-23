import sys
input = sys.stdin.readline
import heapq

n= int(input())
m= int(input())
ppl=[]
maxN= 0
heap = []
for _ in range(n):
    a = int(input())
    ppl.append(a)
    heapq.heappush(heap, a)
    maxN = max(maxN, a)
for i in range(m):
    ans = heapq.heappop(heap)
    ans +=1
    heapq.heappush(heap, ans)
print(max(heap), maxN + m)
