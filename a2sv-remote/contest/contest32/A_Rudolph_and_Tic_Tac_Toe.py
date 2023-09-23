import sys
input = sys.stdin.readline
# from collections import Counter

t= int(input())


def found(arr):
    # check rows
    for i in range(3):
        if arr[i][0] ==arr[i][1] == arr[i][2]:
            if arr[i][0] !='.':
                return arr[i][0]
    # check cols
    for i in range(3):
        if arr[0][i] ==arr[1][i] == arr[2][i]:
            if arr[0][i] !='.':
                return arr[0][i]
    
    if arr[0][0] == arr[1][1] == arr[2][2]:
        if arr[0][0] !='.':
            return arr[0][0]
    if arr[2][0] == arr[1][1] == arr[0][2]:
        if arr[2][0] !='.':
            return arr[2][0]
    return "DRAW"
for _ in range(t):
    arr= []
    for i in range(3):
        s = input().strip()
        arr.append(s)

    print(found(arr))

    
