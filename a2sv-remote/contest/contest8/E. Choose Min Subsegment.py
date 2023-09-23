# https://codeforces.com/gym/428258/problem/E
import sys
from collections import Counter
input = sys.stdin.readline


n= int(input())
arr = [int(a) for a in input().split()]

d= Counter(arr)


for k,v in d.items():
    if v==1:
        d.pop(k, None)
temp={}
matched=0
l=r=0
ans=sys.maxsize
while r<len(arr):
    temp[arr[r]]= temp.get(arr[r], 0)+1
    if temp[arr[r]]==d[arr[r]]:
        matched+=1
    while matched==len(d):
        ans=min(ans, r-l+1)
        temp[arr[l]]-=1
        if temp[arr[l]] < d[arr[l]]:
            matched-=1
        l+=1
print(ans)



