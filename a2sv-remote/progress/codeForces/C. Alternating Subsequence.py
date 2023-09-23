import sys
input = sys.stdin.readline

def sym(num):
    return num>0

def findMax(arr):
    if len(arr)<2:
        return arr[0]

    tot=0
    l, r = 0,0
    while r < len(arr):
        
        maxN= -sys.maxsize
        
        while r < len(arr) and sym(arr[r]) == sym(arr[l]):
            maxN= max(maxN, arr[r])
            r+=1
        tot+=maxN
        l=r
    return tot

        

n=int(input())


for i in range(n):
    j = int(input())
    s= [int(a) for a in input().split()]
    print(findMax(s))
    # print("------------")

# s= [int(a) for a in input().split()]

# print(findMax(s))