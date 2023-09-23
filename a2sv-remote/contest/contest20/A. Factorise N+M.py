import sys
input = sys.stdin.readline
# from collections import Counter

n= int(input())
for i in range(n):
    k= int(input())
    if k==2 or k==3:
        print(7)
    else:
        print(3)