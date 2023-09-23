import sys
input = sys.stdin.readline


n= int(input())
arr = [int(a) for a in input().split()]

arr.sort()
if arr[0]*2*n==sum(arr):
    print(-1)
else:
    [ print(a, end=" ") for a in arr] 