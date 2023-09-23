import sys
input = sys.stdin.readline
# from collections import Counter
class Solution:
    def __init__(self):
        self.root ={}
        self.d = {}
    def find(self, x):
        if x not in self.root:
            self.root[x]= x
            return x
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    def union(self, old, new):
        oldRoot = self.find(old)
        # update the root continiously
        self.root[new] = oldRoot

        self.d[oldRoot]=new


t= int(input())
sol = Solution()
for i in range(t):
    old, new = input().split()
    sol.union(old, new)
ans = []

for k, v in sol.root.items():
    if k==v:
        ans.append(f'{k} {sol.d[k]}')
print(len(ans))
for i in ans:
    print(i)