import sys
input = sys.stdin.readline


n= int(input())
arr = [int(a) for a in input().split()]

l,r=0,n-1

ser=0
dim=0
while r>=l:

    ser+= max(arr[l], arr[r])
    if arr[l]> arr[r]:
        l+=1
    else:
        r-=1
    if r>=l:
        dim+= max(arr[l], arr[r])
        if arr[l]> arr[r]:
            l+=1
        else:
            r-=1
print(ser, dim)