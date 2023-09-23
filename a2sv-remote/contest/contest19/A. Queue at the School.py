import sys
input = sys.stdin.readline
# from collections import Counter


n,t = [int(a) for a in input().split()]
arr = [a for a in input().strip()]
# print(t, arr)
for i in range(t):
    ctr=0
    cpArr=arr[:]
    for j in range(1,len(arr)):
        k=j-1
        if arr[k]=='B' and arr[j]=='G':
            cpArr[j],cpArr[k]=cpArr[k], cpArr[j]
            ctr+=1
            # print("swap", k,j)
    arr=cpArr
    if ctr==0:
        break
print(''.join(arr))
        

