class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges) +1
        
        self.root = [i for i in range(n)]
        self.size = [1] * n
        
        for u,v in edges:
            ret = self.union(u, v)
            if ret[2]:
                return [ret[0], ret[1]]
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
            return [x, y, False]
        else:
            return [x, y, True]
                
                