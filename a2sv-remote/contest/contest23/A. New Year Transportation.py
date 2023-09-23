# https://codeforces.com/gym/444629/problem/A

import sys
input = sys.stdin.readline
# from collections import Counter


n, t = [int(a) for a in input().split()]
a = [int(a) for a in input().split()]

    
def find(v):
    if v==t:
        # print("----",v,t)
        return True
    if v>t:
        return False
    return find(v+a[v-1])
if find(1):
    print("YES")
else:
    print("NO")