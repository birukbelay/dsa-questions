import sys
input = sys.stdin.readline
from collections import Counter

n= int(input())
s = input().strip()

st = s.lower()

ctr = Counter(st)
if len(ctr)==26:
    print("YES")
else:
    print("NO")