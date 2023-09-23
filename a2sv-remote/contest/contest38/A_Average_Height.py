import sys
input = sys.stdin.readline
# from collections import Counter

t= int(input())

for _ in range(t):
    oddList=[]
    evenList=[]
    n= int(input())
    arr = [int(a) for a in input().split()]
    for itm in arr:
        if itm%2==0:
            evenList.append(itm)
        else:
            oddList.append(itm)
    ans= oddList + evenList
    print(*ans)