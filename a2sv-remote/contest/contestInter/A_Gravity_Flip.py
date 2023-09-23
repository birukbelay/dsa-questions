import sys
input = sys.stdin.readline
# from collections import Counter

n= int(input())
arr = [int(a) for a in input().split()]

maxL= max(arr)

new =[0]*maxL
matrix= []
for i in range(maxL):

    for j in range(len(arr)):
        if arr[j]>0:
            arr[j]-=1
            new[i]+=1

new2= [0] * len(arr)
for i in range(len(new)):
    for j in range(new[i]):
        new2[j]+=1

res = new2[::-1]
print(*res)
