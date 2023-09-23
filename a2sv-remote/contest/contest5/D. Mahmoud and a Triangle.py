import sys
input = sys.stdin.readline


n= int(input())
arr= input().split()

def trig(arr):
    if len(arr) <3:
        print("NO")
        return
    iarr = [int(a) for a in arr]

    iarr.sort( reverse=True)
    for i in range(len(iarr)-2):
        if iarr[i]< (iarr[i+1]+ iarr[i+2]):
            print("YES")
            return
        print("NO")

        







