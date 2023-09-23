import sys
input = sys.stdin.readline
s = input().strip()

stack=[]
m=0
ctr=0
for i in range(len(s)):
    if s[i]=='(':
        stack.append(s[i])        
    else:
        # print(s[i], len(stack))
        if stack:
            ctr+=2            
            m=max(ctr,m)
            stack.pop()
        else:            
            ctr=0
print(m)


