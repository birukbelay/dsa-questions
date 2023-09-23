# https://codeforces.com/gym/444629/problem/C
import sys
input = sys.stdin.readline
from collections import defaultdict

d=defaultdict(list)
n, m = [int(a) for a in input().split()]
arr = [[int(a), 0] for a in input().split()]
# updating the tuples second balues
for i in range(len(arr)):
    arr[i][1]=i+1
arr.sort()
for i in range(m):
    
    f1,f2 = [int(a) for a in input().split()]
    d[f1].append(f2)
    d[f2].append(f1)

heard=set()
cost=0
def spread(v):
    if v in heard:
        return
    if idx>= n:
        return
    heard.add(v)
    if len(heard)==n:
        return
    
    for i in d[v]:
        spread(i)
idx=0
# print("--",d)
# print("--|",arr)
while len(heard)<n and idx<n:
    if arr[idx][1] not in heard:
        
        cost+=arr[idx][0]
    spread(arr[idx][1])
    idx+=1
        
    
print(cost)