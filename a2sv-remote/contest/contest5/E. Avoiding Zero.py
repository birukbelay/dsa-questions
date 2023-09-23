import sys
input = sys.stdin.readline


n= int(input())
def cal(n):
    for i in range(n):
        v= int(input())
        arr = input().split()
        iarr = [int(a) for a in arr]
        su= sum(iarr)
        
        if su==0:
            print("NO")
            continue
        elif su>0:
            iarr.sort(reverse=True)
        else:
            iarr.sort()

        while iarr[0]==0:
            iarr[0], iarr[-1]= iarr[-1], iarr[0]
        print("YES")
        for i in iarr:
            print(i, end=" ")
        print()
        # print(iarr)
cal(n)