class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        self.root={}
        self.size= defaultdict(int)
        
        
        for x,y in pairs:
            self.union(x,y)
        group = defaultdict(list)
        letGrp = defaultdict(list)
        for k, v in self.root.items():
            ro = self.find(k)
            heapq.heappush(letGrp[ro], s[k])
            heapq.heappush(group[ro], k)
            # letGrp[v].append()
            
            # group[v].append([k, s[k]])
        # print(self.root)
        # print(group)
        # print(letGrp)
        ans =[a for a in s]
        
        for k,arr in group.items():
            numArr= arr
            
            letArr = letGrp[k]
            
            while numArr:
                let = heapq.heappop(letArr)
                num = heapq.heappop(arr)
                ans[num]= let
        return ''.join(ans)
            
        
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