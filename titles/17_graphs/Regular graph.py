import sys
input = sys.stdin.readline
from collections import defaultdict

n,m  = [int(a) for a in input().split()]
d= defaultdict(list)


def ans():
    if m ==0:
        return "YES"
    for  i in range(m):
        a, b = [int(a) for a in input().split()]
        d[a].append(b)
        d[b].append(a)
    a=sorted(d.items())
    base= a[0][1]
    
    for k, val in a:
        if len(val)!=len(base):
            return 'NO'
            
    return 'YES'



print(ans())
