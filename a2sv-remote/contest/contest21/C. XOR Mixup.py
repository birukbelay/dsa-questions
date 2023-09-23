
import sys
input = sys.stdin.readline
# from collections import Counter

n= int(input())
for i in range(n):
    j= int(input())
    arr = [int(a) for a in input().split() ]
    
    for i in range(j):
        num=0
        for k in range(j):
            if k!=i:
                num^=arr[k]
        if arr[i]==num:
            print(num)
            break
            