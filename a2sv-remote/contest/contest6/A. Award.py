#
import sys
input = sys.stdin.readline


s = input().split()

n= int(s[0])
k = int(s[1])
m= int(s[2])

if n< min(k,m):
    print("YES")
else:
    print("NO")
    