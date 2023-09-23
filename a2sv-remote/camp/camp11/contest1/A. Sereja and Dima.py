# https://codeforces.com/gym/431213/problem/A
import sys
input = sys.stdin.readline
# from collections import Counter

n= int(input())
arr = [int(a) for a in input().split()]

l,r=0,len(arr)-1

s=d=0

i=0
while r>=l:
    if i==0:
        if arr[l]>arr[r]:
            s+=arr[l]
            l+=1
        else:
            s+=arr[r]
            r-=1
        i=1
    else:
        if arr[l]>arr[r]:
            d+=arr[l]
            l+=1
        else:
            d+=arr[r]
            r-=1
        i=0
print(s,d)
        