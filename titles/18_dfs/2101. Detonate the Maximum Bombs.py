class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # make a bomb dictionary with index of the bomb
        # 
        
        d=defaultdict(list)
        def dist(x1, y1, x2, y2):
            return (x1-x2)**2 + (y2-y1)**2
            
        
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                
                x1,y1, r1= bombs[i]
                x2,y2, r2= bombs[j]
                if i!=j:
                    if dist(x1,y1, x2, y2) <= r1**2:
                        d[i].append( j)
        
        def dfs(node, visited):
            visited.add(node)
            count =1
            for nbr in d[node]:
                if nbr not in visited:
                    count+= dfs(nbr, visited)
            return count
        maxN=1
        for node in range(len(bombs)):
            visited=set()
            count= dfs(node, visited)
            maxN=max(maxN, count)
        
            
            
            
        return maxN 
            
            
        
        