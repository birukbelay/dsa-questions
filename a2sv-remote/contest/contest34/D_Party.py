import sys
input = sys.stdin.readline
from collections import defaultdict
class soln:
    def __init__(self):
        self.root = {}
        self.size= defaultdict(int)
    def find(self, node):
        if node not in self.root or node ==self.root[node]:
            self.root[node] = node
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


n = int(input())
k = int(input())
friends = defaultdict(list)
hates = defaultdict(list)

# creating union of all friends groups
friends = soln()
for _ in range(k):
    u, v = [int(j) for j in input().strip()]
    friends.union(u, v)





# make a graph of people that hate each other
m = int(input())
for _ in range(m):
    u, v = [int(j) for j in input().strip()]
    hates[u].append(v)
    hates[v].append(u)


# create a friends group array,to put all friends in one array
groups = defaultdict(set())

for k,v in friends.root.items():
    root = friends.find(k)
    groups[root].add(k)
#remove groups that have hating friends
for k,v in hates.items():
    for item in v:
        #check if 2 ppl that hate are in the same grp
        root = friends.find(k)
        if friends.find(item) == root:
            groups.pop(root, None)
        
