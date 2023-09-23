# https://codeforces.com/gym/437545/problem/C
import sys
input = sys.stdin.readline
# from collections import Counter


n,d = [int(a) for a in input().split()]
arr= [int(a) for a in input().split()]
cnt=len(arr)
r=len(arr)-1
ctr=0
while cnt>0:
    if d>arr[-1]:
        big=d//arr[-1]
        if cnt>=big+1:
            cnt-=big+1
            ctr+=1
            arr.pop()
        else:
            cnt=0
    else:
        ctr+=1
        arr.pop()
        cnt-=1

print(ctr)