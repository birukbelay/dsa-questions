# https://codeforces.com/gym/431213/problem/D
import sys
input = sys.stdin.readline
# from collections import Counter

n,m,k = input().split()

arr = [int(a) for a in input().split()]

empt=[0]* len(arr)

# make the addition operation
for i in range(int(m)):
    op=[int(a) for a in input().split()]
    l,r,d= op[0],op[1],op[2]

    empt[l-1]+=d
    empt[r]-=d
# create a prefix sum
for i in range(1,len(empt)):
    empt[i]+=empt[i-1]



"""
on question D, if for a given query x[i]=3 and y[i]=5, 
it means you should apply operations with index b/n 3 to 5 once.


so op 3 once, op 4, once , op 5 once
"""