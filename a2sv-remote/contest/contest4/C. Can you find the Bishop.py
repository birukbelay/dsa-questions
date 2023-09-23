import sys
input = sys.stdin.readline


n= int(input())

for i in range(n):
    x=input()
    b=[]
    for i in range(8):
        s = input().strip()
        b.append(s)
    for i in range(1,7):
        for j in range(1,7):
            if b[i][j]=="#":
                if b[i-1][j-1]=="#" and b[i+1][j+1]=="#" and b[i-1][j+1]=="#" and b[i+1][j-1]:
                    print(i+1, j+1)