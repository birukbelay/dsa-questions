# https://codeforces.com/problemset/problem/977/C?locale=en


import sys
input = sys.stdin.readline



n, k = input().split()
arr = [int(a) for a in input().split()]
arr.sort()

v=int(k)-1
if k==n:
    print(arr[v])
elif arr[v] == arr[v+1]:
    print(-1)
else:
    print(arr[v])


