import sys
input = sys.stdin.readline


v= input().split()

s = int(v[0])
n= int(v[1])
def win(s, n):
    s=s
    newArr=[]
    for i in range(n):
        d= input().split()
        newArr.append((int(d[0]), int(d[1])))
    newArr.sort()
    for i in newArr:  
        if s> int(i[0]):
            s+= int(i[1])
        else:
            print("NO")
            return
    print("YES")
win(s,n)

