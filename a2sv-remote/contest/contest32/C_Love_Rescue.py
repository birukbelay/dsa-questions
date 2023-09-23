import sys
input = sys.stdin.readline
class Solution:

    def __init__(self):
        self.root={}
        self.size = {}
        for i in range(26):
            self.root[chr(97+i)]= chr(97 +i)
            self.size[chr(97+i)]= 1
        

        
    def find(self, node):
        while node !=self.root[node]:
            node= self.root[node]
        return node
        # return self.root[node]
    def union(self, x, y):   
        print("x,y--",x, y)
        rootX= self.find(x)
        rootY = self.find(y)       
        print("root x ---",rootX, rootY)
        if self.root[rootX] != self.root[rootY]:
            if self.size[rootX] > self.size[rootY]:
                self.root[rootY] = x
                self.size[rootX] += self.size[rootY]
                self.size[x] += self.size[y]
            else:
                self.root[rootX] = y
                self.size[rootY] += self.size[rootX]
                self.size[y] += self.size[rootX]



n = int(input())
w1 = input().strip()
w2 = input().strip()
print(w1, w2)
sol = Solution()

for i in range(n):
    sol.union(w2[i],w1[i])
col = []

for i in range(n):
    if sol.size[w1[i]]==1:
        print(w1[i])
        col.append(w1[i])
    if sol.size[w2[i]]==1:
        print(w2[i])
        col.append(w1[i])
print("----",col)
print("-",sol.root)
print(sol.size)
