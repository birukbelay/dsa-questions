import sys
input = sys.stdin.readline


arr= input().split()

cap = int(arr[1])

tvs = input().split()

itvs =[int(a) for a in tvs]

itvs.sort()

ans=0
for i in range(cap):
    if itvs[i]<0:
        ans+=itvs[i]
print(abs(ans))