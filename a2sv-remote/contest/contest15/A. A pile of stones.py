# https://codeforces.com/gym/436386/problem/A
import sys
input = sys.stdin.readline
 
n=int(input())
ston=0
# pos=0

s=input().strip()
for i in s:
    if i=="-":
        ston-=1
    else:
        ston+=1
    if ston<0:
        ston=0
print(ston)
