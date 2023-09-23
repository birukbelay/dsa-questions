import sys
input = sys.stdin.readline
from collections import Counter

n= int(input())
arr = [int(a) for a in input().strip()]


ctr= Counter(arr)
c1 = ctr[1]
c0 = ctr[0]

print(n- (2* min(c1, c0)))