import sys
input = sys.stdin.readline
# from collections import Counter

n= input().strip()
vals = {"H", "Q", "9"}
val = True
for i in n:
    if i in vals:
        val = False
if val:
    print("NO")
else:
    print("YES")
