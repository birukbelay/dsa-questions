# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        self.root = [i for i in range(n+1)]
        self.size = [1] * (n+1)
        self.ans = sys.maxsize
        
        for a,b,z in roads:
            self.union(a,b)
        
        for x,y, z in roads:
            if self.find(1)== self.find(x):
                self.ans= min(self.ans, z)
        return self.ans
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX !=rootY:
            if self.size[rootX] > self.size[rootY]:
                self.root[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            else:
                self.root[rootX] = rootY
                self.size[rootY] += self.size[rootX]
            
    