import sys
input = sys.stdin.readline


n= int(input())
s = input().split()
s=list(set(s))
s=[int(i) for i in s]
s.sort()
cnt=0
for i in range(1,len(s)):
    if (int(s[i])- int(s[i-1])) ==1:
        cnt+=1
        if cnt>=2:
            print("YES")
            break
    else:
        cnt=0