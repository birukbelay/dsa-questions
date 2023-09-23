import sys
input = sys.stdin.readline


s = input().split()

n=int(s[0])
l=int(s[1])

pts= input().split()
p= [int(i) for i in pts]
p.sort()
maxR= max(p[0], l-p[-1])

for i in range(1, n):
    r= (p[i]-p[i-1])/2
    maxR = max(maxR, r)

print(maxR)