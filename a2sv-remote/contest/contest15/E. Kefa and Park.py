import sys
input = sys.stdin.readline
 
n,m=[int(a) for a in input().split()]

a=[int(a) for a in input().split()]
arr=[[]]*n
print(arr)
for i in range(n-1):
    n,m=[int(a) for a in input().split()]
    print(arr)
    print("-",n,m)
    arr[n]=arr[n].append(m)
print(arr)