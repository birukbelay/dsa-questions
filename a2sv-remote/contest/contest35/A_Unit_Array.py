import sys
input = sys.stdin.readline
from collections import Counter

t= int(input())

for _ in range(t):

    n = int(input())
    arr = [int(a) for a in input().split()]

    ctr = Counter(arr)
    ctr[-1] = ctr.get(-1, 0)
    ctr[1] = ctr.get(1, 0)
    
    # print(ctr)
    ans=0
    # case 1: no of -1 is more than 1
    if ctr[-1]> ctr[1]:
        diff = ctr[-1] - ctr[1]
        
        ans = (diff%2) + (diff//2)
        #if no of -1 is even
        if ctr[-1]%2 ==0:
            if ans %2 !=0:
                ans+=1
        else:
            if ans %2 ==0:
                ans+=1
    # case 2: no of 1 is more than -1
    elif ctr[-1] < ctr[1]:
        if ctr[-1]%2 !=0:
            ans =1
    # case 3: they are equal
    else:
        if ctr[-1]%2!=0:
            ans =1
    print(ans)

    
    




