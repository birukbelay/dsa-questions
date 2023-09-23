import sys
input = sys.stdin.readline
# from collections import Counter
import heapq

t= int(input())
for _ in range(t):
    heap =[]
    nVid, sec = [int(a) for a in input().split()]
    duration = [int(a) for a in input().split()]
    entertain = [int(a) for a in input().split()]

    for i in range(nVid):
        heapq.heappush(heap, (-entertain[i], duration[i]+i, i+1))
    while heap and  heap[0][1]> sec:
        heapq.heappop(heap)
    if heap:
        print(heap[0][2])
    else:
        print(-1)
    
