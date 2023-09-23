# https://codeforces.com/gym/437545/problem/A
import sys
input = sys.stdin.readline
# from collections import Counter

n= int(input())
arr = [int(a) for a in input().split()]


maxT=1

cur=1

for i in range(1,n):
    if arr[i]>=arr[i-1]:
        cur+=1
    else:
        cur=1
    maxT=max(maxT, cur)
print(maxT)