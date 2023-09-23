import sys
input = sys.stdin.readline


N= int(input())

for i in range(N):
    n=int(input())
    arr = [int(a) for a  in input().split()]
    l,r=0,n-1
    newArr=[0]*n
    ctr=0
    while r>=l:
        newArr[ctr]=arr[l]
        ctr+=1
        if ctr<n:
            newArr[ctr]=arr[r]
        ctr+=1
        l+=1
        r-=1
    [ print(a, end=" ") for a in newArr]
    print()
    

