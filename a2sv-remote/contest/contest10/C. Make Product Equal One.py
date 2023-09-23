# https://codeforces.com/gym/430578/problem/C

import sys
input = sys.stdin.readline





n= int(input())
arr = [int(a) for a in input().split()]
#change all numbers to -1 of +1

ctr=0
zctr=0
nctr=0


for i in arr:
    if i>0:        
        ctr+=i-1
    elif i<=0:
        nctr+=1
        ctr+= abs(i+1)
    else:
        zctr+=1

if nctr%2==0:
    print(zctr+ctr)
else:
    print(ctr+zctr+2)