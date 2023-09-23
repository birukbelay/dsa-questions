import sys
input = sys.stdin.readline
s = input().strip()
 
arr=list(s)
arr.sort()
l=0
d={}
stack=[]
u=''
for i in range(len(s)):
    v=s[i]
    if v!=arr[l]:
        stack.append(v)
        d[v]=d.get(v,0)+1
    else:
        u+=v
        l+=1
    while l<len(arr) and arr[l] in d and d[arr[l]]>0:
        cur=stack.pop()
        u+=cur
        d[cur]-=1
 
 
print(u)