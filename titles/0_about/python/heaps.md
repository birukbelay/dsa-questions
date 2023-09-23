## heaps


import heapq

```py
heapArr=[]
val=1

heapify(heapArr, index)
heapq.heappush(heapArr, val)
heapq.heappop(heapArr)

def LChildIndex( index):
        return 2*index +1  
def RChildIndex(index):
        return 2*index +2
def getParentIndex(index):
        if index==0: return 0
        return (index-1)//2
def isLeaf(i, n):
    return 2*i +2 > n  # the last non leaf index== 2*i +2
def lastNonLeaf(a):
    return len(a)-2//2 

```