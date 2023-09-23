import sys
input = sys.stdin.readline
from collections import deque

q=deque()


s = input().strip()

cur=""
for i in range(len(s)):
    q.append(s[i])
    
    while len(q)>1 and q[-1]==q[-2]:
        cur=q.pop()
        q.pop()
    # while len(q)>1 and cur==q[-1]:
    #     v=q.pop()
        # print(i,"-",v)
print(''.join(q))
    


# newS=""
# cur=s[0]
# ctr=0
# for i in range(1,len(s)):
#     if s[i]==cur:
#         ctr+=1
#     else:
#         if ctr<1:
#             newS+=cur
#         cur=s[i]
#         ctr=0
# print(newS)

        
    
