import sys
input = sys.stdin.readline
# from collections import Counter

n= int(input())
for _ in range(n):
    maxL=0
    s = input().strip()
    l,r=0,0

    while r<len(s):
        
        
        # if r>=len(s):
        #     break
        if s[r]=='R':
            l=r+1
        maxL= max(maxL, r-l+1)
        r+=1

    print(maxL+1)