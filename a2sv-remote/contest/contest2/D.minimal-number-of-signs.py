# https://codeforces.com/gym/420178/submission/188628376
import sys
input = sys.stdin.readline

def getVal(v):
    if v=="#":
        return "?"
    elif v=="?":
        return "x"
    else: return v
d={}
n= int(input())
for i in range(n):
    
    s = input().strip()
    
    for i in range(len(s)):
        if i in d:
            if s[i] ==d[i] or s[i] == "?" or d[i] =='#':
                pass
            # d[i] could be any thing so give the value of s[i]
            elif d[i]=='?':
                
                d[i]=s[i]
            #means d[i] && s[i] have different values
            else: d[i]='#'
        else:
            
            d[i]=s[i]
arr= [0] * len(d)

for k,v in d.items():
    arr[k]=getVal(v)
print("".join(arr))

