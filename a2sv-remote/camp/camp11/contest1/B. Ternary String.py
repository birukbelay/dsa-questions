# https://codeforces.com/gym/431213/problem/B
import sys
input = sys.stdin.readline
# from collections import Counter

n= int(input())


for i in range(n):

    num= input().strip()
    d={}
    l=r=0
    mlen=sys.maxsize
    while r<len(num) :
        
        d[num[r]]= d.get(num[r], 0)+1
        

        while len(d)==3:
            mlen=min(mlen, r-l+1)
            d[num[l]]-=1
            if d[num[l]]==0:
                del d[num[l]]
            l+=1
        r+=1
    if mlen==sys.maxsize:
        print(0)
    else:
        print(mlen)
        
