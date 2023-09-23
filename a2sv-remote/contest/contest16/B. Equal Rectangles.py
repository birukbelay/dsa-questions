# https://codeforces.com/gym/437545/problem/B
import sys
input = sys.stdin.readline
# from collections import Counter

n= int(input())


for i in range(n):
    s= int(input())
    arr = [int(a) for a in input().split()]
    arr.sort()
    ctr=0
    newArr=[]
    for i in range(1, len(arr), 2):
        if arr[i]==arr[i-1]:
            ctr+=1
            newArr.append(arr[i])
    l,r=0,len(newArr)-1
    temp=newArr[0]*newArr[-1]
    flag=True
    while l<r:
        if newArr[l]*newArr[r]!=temp:
            flag=False
        l+=1
        r-=1

    if ctr==s*2 and flag:
        print("YES")
    else:
        print("NO")