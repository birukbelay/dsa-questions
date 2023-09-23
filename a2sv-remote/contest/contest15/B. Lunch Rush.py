import sys
input = sys.stdin.readline

n,k=[int(a) for a in input().split()]

maxJ=- sys.maxsize
for i in range(n):
    f,t= [int(a) for a in input().split()]
    j=0
    if t>k:
        j=f-(t-k)
    else:
        j=f
    maxJ=max(j, maxJ)
print(maxJ)