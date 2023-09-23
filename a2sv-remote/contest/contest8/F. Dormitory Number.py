# https://codeforces.com/gym/428258/problem/F

import sys
input = sys.stdin.readline
# from collections import Counter

n, m= [int(a) for a in input().split()]
rooms = [int(a) for a in input().split()]
letters = [int(a) for a in input().split()]

prefix=[rooms[0]]
for i in range(1, len(rooms)):
    prefix.append(rooms[i]+prefix[i-1])
# print(prefix)
tot=l=0

for i in range(len(letters)):
    tot+=letters[i]
    # print("li", letters[i], "tot", tot)
    while l<len(prefix)-1 and letters[i]- prefix[l]>0:
        l+=1 
    idx= prefix[l-1] if l>0 else 0
    print(l+1, letters[i] - idx)


# input 
# 3 6
# 10 15 12
# 1 9 12 23 26 37