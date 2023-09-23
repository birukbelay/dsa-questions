# https://leetcode.com/problems/find-if-path-exists-in-graph/


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = defaultdict(list)
        
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        visited = set()
        
    
        def dfs(src, visited):
            
            if src== destination:
                return True
            visited.add(src)
            for v in graph[src]:
                if v not in visited:
                    found = dfs(v, visited)
                    
                    if found:
                        return True
            return False
        return dfs(source, visited)
            
                
            

        