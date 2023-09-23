import sys
input = sys.stdin.readline
import heapq
from collections import defaultdict

d=defaultdict(list)
n, m = [int(a) for a in input().split()]
for _ in range(m):
    node1, node2  = [int(a) for a in input().split()]
    d[node1].append(node2)
    d[node2].append(node1)

flag=0

total=defaultdict(int)
for key, val in d.items():
    total[len(val)]+=1
    
if tot[2]==n:
    print('ring topology')    
elif tot[2]==n-2 and tot[1]==2:
    print('bus topology')    
elif tot[1]==n-1 and tot[n-1]==1:
    print('star topology')
else:
    print('unknown topology')
