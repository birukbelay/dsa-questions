# https://codeforces.com/gym/430578/problem/D

import sys
input = sys.stdin.readline
# from collections import Counter

n= int(input())
arr = [int(a) for a in input().split()]
newArr=[]
for i,v in enumerate(arr):
    newArr.append((v,i))
newArr.sort()
ctr=n-1
print(ctr)
while ctr>0:
    print(newArr[ctr][1], ctr)
    ctr-=1
