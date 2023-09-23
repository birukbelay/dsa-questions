import sys
input = sys.stdin.readline
from collections import Counter

n, k = [int(a) for a in input().split()]
sarr = [int(a) for a in input().split()]

ctr= Counter(sarr)

def find():
    if k==n:
        return sarr
    
    srt = sorted(ctr.items(), key=lambda item: item[1], reverse=True)
    if len(srt)>=k:
        

