class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        ancestors = [ set() for _ in range(n)]
        
        graph = [[] for _ in range(n)]
        
        
        incoming = [0 for _ in range(n)]
        
        for parent, child in edges:
            graph[parent].append(child)
            incoming[child] +=1
        
        que = deque()
        
        for node in range(n):
            if incoming[node]== 0:
                que.append(node)
        
        while que:
            node = que.popleft()
            # ansestors[node].update(ans[node])
            
            for child in graph[node]:
                incoming[child] -=1
                ancestors[child].add(node)
                ancestors[child].update(ancestors[node])
                if incoming[child]==0:
                    que.append(child)
        ans = [[] for _ in range(n)]
        
        for i in range(n):
            ans[i]= sorted(list(ancestors[i]))
        return ans
            
        
        