import sys
input = sys.stdin.readline


n= int(input())

for i in range(n):
    def func():
        v= int(input())
        s= input().split()
        iarr = [int(a) for a in s]
        iarr.sort()
        
        for i in range(1, v):
            if iarr[i] - iarr[i-1] >1:
                print("NO")
                return
        print("YES")
    func()
        
            
        