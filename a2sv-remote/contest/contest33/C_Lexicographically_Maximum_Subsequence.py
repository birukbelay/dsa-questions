import sys
input = sys.stdin.readline
import heapq

heap = []
arr =input().strip()

for i in range(len(arr)):
    big = -ord(arr[i])
    heapq.heappush(heap,(big, arr[i], i) )
ans =''
pos=-1
while heap:
    _, val, idx = heapq.heappop(heap)
    if idx>pos:
        ans+= val
        pos= idx
print(ans)
    


