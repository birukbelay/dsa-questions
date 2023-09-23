import sys
input = sys.stdin.readline


n= int(input())

for i in range(n):
    r1 = input().split()
    r2 = input().split()

    r1l= max(int(r1[0]), int(r1[1]))
    r1w = min(int(r1[0]), int(r1[1]))
    
    r2l= max(int(r2[0]), int(r2[1]))
    r2w = min(int(r2[0]), int(r2[1]))

    if r1w +r2w == r1w and r1l==r2l:
        print("YES")
    else:
        print("NO")



