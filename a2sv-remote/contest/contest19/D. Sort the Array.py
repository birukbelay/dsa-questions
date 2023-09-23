import sys
input = sys.stdin.readline
# from collections import Counter

n= int(input())
arr = [int(a) for a in input().split()]

idx=-1
idx2=-1
re=False
ctr=0
error=False
for i in range(1,len(arr)):
    j=i-1
    if idx ==-1 and arr[j]>arr[i]:
        idx=j
        re=True
        continue
    if ctr==0 and idx!=-1 and arr[j]<arr[i]:

        idx2=j
        re=False
        ctr=1
        continue
    if ctr>0 and arr[j]>arr[i]:
        error=True
        break
if error:
    print("no")
else:
    if idx==-1:
        print("yes")
        print(1, 1)
    elif idx2==-1:
        print('yes')
        print(idx+1, len(arr))
    else:
        l,r=idx, idx2
        err=False
        while l<r:
            arr[l], arr[r]=arr[r], arr[l]
            l+=1
            r-=1
        for i in range(1,len(arr)):
            if arr[i]< arr[i-1]:
                err=True
                break
        if err:
            print('no')
        else:
            print('yes')
            print(idx+1, idx2+1)
    

