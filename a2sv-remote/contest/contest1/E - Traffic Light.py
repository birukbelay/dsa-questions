import collections
import sys
input = sys.stdin.readline


def light(s, b):
    j = len(b)
    
    
    q = collections.deque()
    for i, v in enumerate(b):        
        if v == "g":
            q.append(i)            
    lastG = q[-1] # to check if there is a value greater than last g
    firstG = q[0] # to calculate the nxt g for the val which is greater than last g
    

    dis = 0 
    if s!="g":
        for i, v in enumerate(b):
            if v == s:
                if i < firstG:
                    dis = max(dis, firstG - i)
                    # print(dis)
                elif i > lastG:
                    dis = max(dis, (j-i) + firstG)
                    # print("---",j,(j-i),i , firstG)
                    break                
                else:
                    # remove all g less than i
                    while q and q[0] < i:
                        q.popleft()
                    dis = max(dis, q[0] - i)
    print(dis)


n= int(input())

for i in range(n):
    x, symb = input().split()
    s= input().strip()
    light(symb, s)


# light("r", "rggry")
