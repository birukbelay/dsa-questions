import sys
input = sys.stdin.readline
# from collections import Counter

n= int(input())
arr = [int(a) for a in input().split()]
arr.sort()

ctr=0
sum=0
carry=0
while arr and arr[-1]==4:
    ctr+=1
    arr.pop()
l,r=0,len(arr)-1
while l<r:
    sum=arr[l]+arr[r]
    if sum==4:
        ctr+=1
        l+=1
        r-=1
        continue
    while l<r and sum < 4:
        l+=1
        if sum+arr[l]<4:
            sum+=arr[l]
        elif sum+ arr[l]==4:
            ctr+=1
            l+=1            
            break
    ctr+=1
    r-=1

    


if r==l:
    ctr+=1
print(ctr)
