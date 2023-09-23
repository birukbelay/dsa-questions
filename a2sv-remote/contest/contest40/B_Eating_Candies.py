import sys
input = sys.stdin.readline
from collections import deque

t= int(input())
for _ in range(t):
    n= int(input())
    arr = [int(a) for a in input().split()]

    flag=1

    q= deque(arr)
    ctr=0
    leftSum =0
    rightSum =q.pop()

    while q:

        if flag:
            while q and rightSum > leftSum:
                leftSum += q.popleft()
            flag =0
        else:
            while q and leftSum> rightSum:
                rightSum += q.pop()
            flag=1
        if rightSum ==leftSum:
            ctr=n-len(q)
            if q:
                rightSum += q.pop()
                flag=1
    print(ctr)







