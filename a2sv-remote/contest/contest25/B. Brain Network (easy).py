import sys
input = sys.stdin.readline().strip()
from collections import defaultdict

# n= int(input())
n, m = [int(a) for a in input().split()]
d=defaultdict(list)
for i in range(m):
    a, b = [int(a) for a in input().split()]

    d[a].append(b)
    d[b].append(a)

visited= set()

