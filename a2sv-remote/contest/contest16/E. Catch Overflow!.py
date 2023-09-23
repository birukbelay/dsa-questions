# https://codeforces.com/gym/437545/problem/E
import sys
input = sys.stdin.readline
# from collections import Counter

n= int(input())
stack=[1]
res=0
for i in range(n):
    s=input().split()
    if s[0]=='add':
        res +=stack[-1]
    elif s[0] == 'for':
        temp = min(stack[-1]*int(s[1]), 4294967296)
        stack.append(temp)
    elif s[0]== 'end':
        stack.pop()
print(res if res <4294967296 else "OVERFLOW!!!")

