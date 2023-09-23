# https://codeforces.com/gym/444629/problem/B


import sys
input = sys.stdin.readline
# from collections import Counter
d={
    "a":1,"b":2, "c":3, "d":4, "e":5, "f":6, "g":7,"h":8
}
s= input().strip()
sr, sc = int(s[1]), d[s[0]]
t= input().strip()
tr, tc = int(t[1]), d[t[0]]

arr=[]
def locate(r, c):
    
    if r==tr and c==tc:
        return True
    
    if tr>r:        
        if c==tc:
            arr.append("U")
            locate(r+1, c)
        elif tc>c:
            arr.append("RU")
            locate(r+1, c+1)
        else:
            arr.append("LU")
            locate(r+1, c-1)
    elif tr==r:
        if tc>c:
            arr.append("R")
            locate(r, c+1)
        else:
            arr.append("L")
            locate(r, c-1)
    else:
        if c==tc:
            arr.append("D")
            locate(r-1, c)
        elif tc>c:
            arr.append("RD")
            locate(r-1, c+1)
        else:
            arr.append("LD")
            locate(r-1, c-1)
            
            
locate(sr,sc)
print(len(arr))
for i in arr:
    print(i)
       
# moves ={"L":(0,-1), "R":(0,1), "U":(1,0), "D":(-1,0), "LU":(1,-1), "LD":(-1,-1), RU:(1,1), RD:(-1,1)}
    
    
    