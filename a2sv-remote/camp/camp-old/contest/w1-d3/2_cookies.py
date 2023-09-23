import heapq

def cookies(k, A):
    # Write your code here
    heapq.heapify(A)
    ctr=0
    if len(A)==1:
        if A[0]>k:
            return 0
        else:
            return -1
    while A[0]<k:
        if len(A)==1:
            if A[0]>k:
                return ctr
            else:
                return -1
        val1=heapq.heappop(A)
        val2=heapq.heappop(A)
        
        new=(val1+2)*val2
        heapq.heappush(A, new)
        ctr+=1
    return ctr
