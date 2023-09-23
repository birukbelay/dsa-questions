import sys
input = sys.stdin.readline
from collections import Counter

n= int(input())
arr = [int(a) for a in input().split()]
tupArr=[]
for i, v, in enumerate(arr):
    tupArr.append((v, i))
tupArr.sort()

if len(arr)==1:
    print(1)
else:
    if tupArr[0][0]== tupArr[1][0]:
        print('Still Rozdil')
    else:
        print(tupArr[0][1]+1)
