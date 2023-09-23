import sys
input = sys.stdin.readline
# from collections import Counter

n= int(input())

memo={}
def fib(n):
    if n==1 or n==0:
        return 1
    
    if n in memo:
        return memo[n]
    # ans = 
    memo[n]= fib(n-1) + fib(n-2)
    return memo[n]
print(fib(n))