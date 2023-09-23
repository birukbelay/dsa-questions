import sys
input = sys.stdin.readline


n= int(input())


for i in range(n):
    N=int(input())
    j = input().strip()
    s=[a for a in j]
    l,r= 0,N-1
    # print(i, N, l,r)
    # print(s)
    while l<r:
        if (s[l]=='0' and s[r]=='1') or (s[r]=='0' and s[l]=='1'):
            l+=1
            r-=1
        else:
            break
    if l==r:
        print(1)
    elif l>r:
        print(0)
    else:
        print(r-l+1)

