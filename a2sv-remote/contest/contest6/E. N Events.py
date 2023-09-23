# TODO https://codeforces.com/gym/425122/problem/E
import sys
input = sys.stdin.readline


n= int(input())
arr=[]
for i in range(n):    
    s = input().split()
    arr.append((int(s[0]), int(s[1])))

arr.sort(key=lambda x: (x[0], -x[1]))
ctr=0

maxN= arr[0][1]
for i in range(n-1):
    if arr[i][1] >maxN:
        maxN = arr[i][1]
    if max > arr[i+1][1]:
        ctr+=1
print(ctr)



ctd=set()


l,r=0,len(arr)

for i in range(len(arr)):
    for j in range(i,len(arr)):

        if arr[j][1] <arr[i][1] and arr[j] not in ctd:
            ctr+=1
            ctd.add(arr[j])

        else:
            break
print(ctr)


