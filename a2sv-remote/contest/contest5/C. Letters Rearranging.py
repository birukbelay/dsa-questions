import sys
from collections import Counter
input = sys.stdin.readline

# aabbaa
v= int(input())

def ispalindrome(s):
    
    l,r=0,len(s)-1
    while l<r:
        if s[l]!=s[r]:
            return False
        l+=1
        r-=1
    # print("pali", s)
    return True

for i in range(v):
    s = input().strip()
    ctr = Counter(s)
    if len(ctr) ==1:
        print(-1)
    else:
        if ispalindrome(s):
            lst =[x for x in s]
            # print(lst)
            lst.sort()
            lst[0],lst[-1]= lst[-1], lst[0]
            print("".join(lst))
            
        else:
            print(s)
            