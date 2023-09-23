import sys
input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()

if s1==s2:
    print('-1')
    exit()
maxL= max(len(s1), len(s2))

print(maxL)