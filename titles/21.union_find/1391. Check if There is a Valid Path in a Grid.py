# https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/
valDir ={
    1: ['l','r'], # left, right
    2: ['u', 'd'], # up , down
    3: ['d', 'l'], # down, left
    4: ['d', 'r'], # down right
    5: ['u', 'l'], #up left
    6: ['u', 'r'], #
}
DIR = {
    'l':[0, -1],
    'r':[0, 1],
    'u':[-1, 0],
    'd':[1, 0],
}

allowed ={
    'l': [1, 4, 6],
    'd' :[2, 5, 6],
    'u': [2, 3, 4],
    'r': [1, 3, 5]

    }
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        self.root = {}
        self.size = defaultdict(int)        
        n, m = len(grid), len(grid[0])
        in_bound = lambda row, col: 0 <= row < n and 0 <= col < m
        def isValidPath(r, c, d):
            # print("--",d, (r,c))
            if in_bound(r,c):
                # print("--2",d, (r,c))
                nxtVal = grid[r][c]
                return  nxtVal in allowed[d]
        
        for i in range(n):
            for j in range(m):
                self.root[(i,j)] = (i,j)
                self.size[(i,j)] =1
        
        for i in range(n):
            for j in range(m):
                val = grid[i][j]
                
                for d in valDir[val]:
                    dirs = DIR[d]
                    nxtNode = (dirs[0] + i, dirs[1] + j )
                    # print((i,j),d, nxtNode)
                    if isValidPath(nxtNode[0], nxtNode[1], d):
                        # print("valid",[i,j], nxtNode)
                        self.union((i,j), nxtNode)
        # print(self.root)
        return self.find((0,0)) == self.find((n-1, m-1))
        
    def find(self, node):
        if node ==self.root[node]:
            return node
        self.root[node] = self.find(self.root[node])
        return self.root[node]
    def union(self, curNode, nxtNode):        

        rootX = self.find(curNode)
        rootY = self.find(nxtNode)

        if rootX != rootY:
            if self.size[rootX] > self.size[rootY]:
                self.root[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            else:
                self.root[rootX] = rootY
                self.size[rootY] += self.size[rootX]
            
        
        