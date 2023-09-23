# https://codeforces.com/contest/664/problem/A
import sys
input = sys.stdin.readline
# from collections import Counter

a,b = [int(a) for a in input().split()]

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
g=0
if a==b:
    print(a)
else :
    g=gcd(b,a)
    # find the gcd of a+1 that is >=g
