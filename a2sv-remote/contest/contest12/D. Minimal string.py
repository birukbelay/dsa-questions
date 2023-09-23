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
        d[arr[l]]-=1
        l+=1
    while stack[-1]<arr[l]:
        cur=stack.pop()
        u+=cur
        
    

    

#     while stack and stack[-1]<v:
#         u+=stack.pop()
#     stack.append(v)
#     while stack:
#     u+=stack.pop()

print(u)

