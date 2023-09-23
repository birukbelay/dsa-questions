import sys
input = sys.stdin.readline


n= int(input())



for i in range(n):
    j = int(input())

    arr = [int(a) for a in input().split()]
    copyArr=arr[:]

    copyArr.sort()
    
    newArr=[]
    for i,v in enumerate(arr):
        if v==copyArr[-1]:
            newArr.append(v-copyArr[-2])
        else:
            newArr.append(v-copyArr[-1])
    [ print(a, end=" ") for a in newArr]
    print()