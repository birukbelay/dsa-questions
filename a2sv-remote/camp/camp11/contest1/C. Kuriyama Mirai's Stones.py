# https://codeforces.com/gym/431213/problem/C
import sys
input = sys.stdin.readline
# from collections import Counter

n= int(input())
# unsorted stones
arr = [int(a) for a in input().split()]
s = int(input())
# sorted array
sarr =arr[:]
sarr.sort()
# make the Prefix sum
for i in range(1, len(arr)):
    arr[i]+=arr[i-1]
for i in range(1, len(arr)):
    sarr[i]+=sarr[i-1]
for i in range(s):
    ans = [int(a) for a in input().split()]
    
    typ,l,r=ans[0], ans[1], ans[2]

    if typ==1:
        lst = 0 if l==1  else arr[l-2]
        print(arr[r-1]-lst)
    else:
        lst = 0 if l==1  else sarr[l-2]
        # print("----",r)
        print(sarr[r-1]-lst)

