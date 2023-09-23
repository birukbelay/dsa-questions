import sys
input = sys.stdin.readline
# from collections import Counter


t= int(input())
for _ in range(t):
    n= int(input())
    arr = [int(a) for a in input().split()]

    mi = min(arr)
    tot= sum(arr)
    print(tot-(mi*n))