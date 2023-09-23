import sys
input = sys.stdin.readline
# from collections import Counter

n= int(input())
costs = [int(a) for a in input().split()]
sums = sorted(costs)
# print("----",costs, sums)

for i in range(1, n):
    sums[i]+= sums[i-1]
for i in range(1, n):
    costs[i]+= costs[i-1]

    
# print("----",costs, sums)


m= int(input())

for i in range(m):
    t, l, r = [int(a) for a in input().split()]
    
    if t==1:
        ans= costs[r-1]- (costs[l-2] if l>1 else 0) 
        print(ans)
    else:
        ans= sums[r-1]- (sums[l-2] if l>1 else 0)
        print(ans)