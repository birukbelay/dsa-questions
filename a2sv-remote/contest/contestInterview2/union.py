


class soln:

    def __init__(self):
        self.root={}
        self.size= defaultdict(int)
        


    def find(self, node):
        if node not in self.root:
            self.root[node] = node
            return node
        if node ==self.root[node]:
            return node
        self.root[node] = self.find(self.root[node])
        return self.root[node]
    def union(self, x, y):        

        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.size[rootX] > self.size[rootY]:
                self.root[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            else:
                self.root[rootX] = rootY
                self.size[rootY] += self.size[rootX]