import sys
input = sys.stdin.readline
# from collections import Counter

n = int(input())
arr = []
d={}
    
for i in range(26):              
    d[chr(i+(ord('a')))]=1


for _ in range(n):
    st = input().strip()
    arr.append(st)

alpha = ""
prev = ""
i = 0
while i< len(arr):
    fst = arr[i][0]
    if d[fst]==1:
        alpha += fst
        d[fst]= 0
        prev= fst
    elif fst == prev:
        # very complicated case handle
        pass
    else:
        print("Impossible")
    i+=1


for key, val in d.items():
    if val==1:
        alpha += key

print(alpha)
    

