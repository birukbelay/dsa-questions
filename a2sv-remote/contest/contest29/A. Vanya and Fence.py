import sys
input = sys.stdin.readline
# from collections import Counter

n, h = [int(a) for a in input().split()]

arr = [int(a) for a in input().split()]

tot = 0

for i in arr:
    if i > h:
        tot+=2
    else:
        tot += 1
print(tot)