# https://codeforces.com/gym/428258/problem/A
import sys
input = sys.stdin.readline
from collections import Counter



n= int(input())
def next(n):
    num=n+1
    s=str(n)
    while num<10000:
        d= Counter(list(str(num)))
        if len(d)==4:
            print(num)
            return
        num+=1
next(8975)
        

    