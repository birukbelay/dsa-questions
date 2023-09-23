# - [] https://codeforces.com/problemset/problem/1675/D
import sys
from collections import defaultdict
input = sys.stdin.readline
 
 
t= int(input())
# - 
def dfs(n, path, seen):    
    if n not in seen:
        path.append(n)
    seen.add(n)
    if n== arr[n-1]:
        return path
    
    dfs(arr[n-1], path,seen)
for i in range(t):
    n = int(input())    
    arr=[int(a) for a in input().split()]
    # Building a dictionary of their children
    d=defaultdict(list)
    root = -1
    for i in range(n):
        parent = arr[i]    
        if parent == i+1:
            root= parent    
        d[parent].append(i+1)
    
    def longest(cur, pre, root, ctrD):
        copy = pre[:]
        copy.append(cur)
        if len(d[cur]) ==0:
            if len(copy)> len(ctrD[root]):
                ctrD[root]= copy
            return
        for node in d[cur]:
            longest(node, copy, root, ctrD)
    ans =[]
    seen = set()
    def returnLongest(root):
        ctr = defaultdict(list)        
        longest(root, [], root, ctr)
        bigChain = ctr[root]
        # add the biggest chain to the answers list
        ans.append(bigChain)

        seen.update(bigChain)
        for itmes in bigChain:
            for child in d[items]:
                if child not in seen:
                    returnLongest(child)
    returnLongest(root)
    print(len(ans))
    for paths in ans:
        print(len(path))
        print(*paht)
        

    # seen = set()
    # mainRoot= returnLongest(root)
    # seen.update(mainRoot)
    # for items in mainRoot:

    #     for childs in d[items]:
    #         if child not in seen:
    #             longChain = returnLongest(child)
    #             seen.update(longChain)





    
    # se=set()
    # ctr=0
    # paths=[]
    # for i in range(n):
    #     path=[]
    #     # if it is a leaf node bcs we are going up
    #     if i+1 not in d:
            
    #         p=dfs(i+1, path, se)
    #         paths.append(path)
            
            
