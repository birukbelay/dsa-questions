import sys
input = sys.stdin.readline
# from collections import Counter

n, t = [int(a) for a in input().split()]
a = [int(a) for a in input().split()]
a.sort()

maxL=0
l=0
# create prefix sum
tot=0

for i in range(n):
    tot += a[i]

    while tot > t:
        tot-=a[l]
        l+=1
    maxL= max(maxL, i-l)

print(maxL+1)