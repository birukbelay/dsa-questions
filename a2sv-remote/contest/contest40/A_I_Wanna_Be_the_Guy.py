import sys
input = sys.stdin.readline
# from collections import Counter
import heapq

n = int(input())

p = [int(a) for a in input().split()]
x = [int(a) for a in input().split()]

s=set()
s.update(p)
s.update(x)
if len(s)==n:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')