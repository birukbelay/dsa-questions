import sys
input = sys.stdin.readline
import heapq
from collections import defaultdict

t= int(input())

for _ in range(t):
    n= int(input())
    ppl = [int(a) for a in input().split()]
    # a place to holde the truth value
    d=defaultdict(int)
    minHeap= []
    maxHeap=[]

    for i in range(len(ppl)):
        d[i+1]=ppl[i]

        heapq.heappush(minHeap, (ppl[i], i+1))
        heapq.heappush(maxHeap, (-1*ppl[i], i+1))
    ans =[]
    # print("--haps", minHeap, maxHeap)
    # print("d", d)
    while minHeap and maxHeap:
        sml, smlIdx= heapq.heappop(minHeap)
        while sml!= d[smlIdx]:
            heapq.heappush(minHeap, (d[smlIdx], smlIdx))
            sml, smlIdx= heapq.heappop(minHeap)
        # print("sml", sml)
        big, bigIdx = heapq.heappop(maxHeap)
        
        while big != (d[bigIdx])*-1:
            # print("in big",big, d[bigIdx])
            heapq.heappush(maxHeap, (d[bigIdx], bigIdx))
            big, bigIdx = heapq.heappop(maxHeap)
        # print("big", big)
        
        pBig= -1*big

        if smlIdx == bigIdx:
            if minHeap and minHeap[0][0] == sml:
                nSml, nIdx = heapq.heappop(minHeap)
                heapq.heappush(minHeap, (sml, smlIdx))
                sml, smlIdx= nSml, nIdx
            elif maxHeap and maxHeap[0][0]==big:
                nbig, nIdx = heapq.heappop(maxHeap)
                heapq.heappush(maxHeap, (big, bigIdx))
                big, bigIdx = nbig, nIdx




        if pBig and sml and (smlIdx!= bigIdx):
            sml-=1
            pBig-=1
            if pBig > 0:
                heapq.heappush(maxHeap, (-1*pBig, bigIdx))
            d[bigIdx]=pBig

            if sml > 0:
                heapq.heappush(minHeap, (sml, smlIdx))
            d[smlIdx]= sml

            ans.append((bigIdx, smlIdx))
    print(len(ans))
    for i in ans:
        print(*i)
        
            


    
    