import sys
input = sys.stdin.readline
# from collections import Counter

n, m ,k = [int(a) for a in input().split()]
arr = []
for i in range(m+1):
    arr.append(int(input()))

def tobin(k):
    arr=[]
    while k>0:
        l=k%2                
        k//=2
        arr.append(l)
    l, r=0, len(arr)-1
    # reverse it
    # while l<r:
    #     arr[l], arr[r]=arr[r], arr[l]
    #     l+=1
    #     r-=1
    return arr

binArr=[]
for i in range(len(arr)):
    bin = tobin(arr[i])
    binArr.append(bin)
fedor = binArr[-1]

frieds=0
for i in range(len(binArr)-1):
    cur = binArr[i]
    dif=abs(len(cur)-len(fedor))
    for i in range(min(len(cur), len(fedor))):
        if fedor[i]!=cur[i]:
            dif+=1
    # print("--", dif)
    if dif<=k:
        frieds +=1
print(frieds)



