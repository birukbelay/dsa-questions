import sys
input = sys.stdin.readline
import heapq
from collections import defaultdict

t= int(input())

for _ in range(t):
    n= int(input())
    ppl = [int(a) for a in input().split()]

    
    maxHeap=[]

    for i in range(len(ppl)):
        if ppl[i]>0:
            heapq.heappush(maxHeap, (-1*ppl[i], i+1))
    ans =[]
    while maxHeap:
        big, bigIdx = heapq.heappop(maxHeap)
        if maxHeap:
            nxtBig, nextIdx = heapq.heappop(maxHeap)
            
            nxtBig+=1
            big+=1
            if big<0:
                heapq.heappush(maxHeap, (big, bigIdx))
            if nxtBig<0:
                heapq.heappush(maxHeap, (nxtBig , nextIdx))
            ans.append((bigIdx, nextIdx))
            
    
    print(len(ans))
    for i in ans:
        print(*i)
        
            


    
    