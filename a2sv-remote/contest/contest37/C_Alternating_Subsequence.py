import sys
# from collections import Counter
input = sys.stdin.readline
 
def check(val):
    return val>0
 
def findMax(arr):
    if len(arr)==1:
        return arr[0]
 
    total=0
    l, r = 0,0
    while r < len(arr):
        
        maxN= -sys.maxsize
        
        while r < len(arr) and check(arr[r]) == check(arr[l]):
            maxN= max(maxN, arr[r])
            r+=1
        total +=maxN
        l=r
    return total
 
        
 
t=int(input())
 
 
for _ in range(t):
    n = int(input())
    arr= [int(a) for a in input().split()]
    print(findMax(arr))