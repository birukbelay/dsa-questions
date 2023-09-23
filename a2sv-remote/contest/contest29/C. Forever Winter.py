import sys
input = sys.stdin.readline
from collections import defaultdict
 
t = int(input())
for _ in range(t):
    n, m = [int(a) for a in input().split()]
    d = defaultdict(list)
    for i in range(m):
        a, b = [int(a) for a in input().split()]
        d[a].append(b)
        d[b].append(a)
    ctr = defaultdict(int)
    # key: len(items)
    #{1: edgeNodes, x:1 }
    for k, v in d.items():
        ctr[len(v)] +=1
    x, z, j = 0,0, 0
    for k, v in ctr.items():
        if v==1:
            x= k
        elif k ==1:
            z= v
        else:
            j= v
    if len(ctr)==3:    
        print(x, z//x)
    elif len(ctr)==2:
        # print("--",ctr, z, j)
        print(j-1, z//(j-1))