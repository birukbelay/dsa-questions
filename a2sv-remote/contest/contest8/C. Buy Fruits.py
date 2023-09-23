import sys
from collections import Counter
input = sys.stdin.readline


n, m = [int(a) for a in input().split()]
arr = [int(a) for a in input().split()]

arr.sort()

fruits=[]
for i in range(m):
    fruits.append(input().strip())
d=Counter(fruits)

minN=0
maxN=0
sd=sorted(d.items(), key=lambda item: item[1], reverse=True)
l=0
r=n-1
for i in sd:
    minN+= arr[l]* i[1]
    l+=1
for i in sd:
    maxN+=arr[r]* i[1]
    r-=1




