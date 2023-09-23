from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		
    # 		colors = [0] * V        
    # 	    def hasCycle(cur, prev):
    #             colors[cur] = 1
    #             for i in adj[cur]:
    #                 if colors[i] !=1:
    #                     if hasCycle(i)
    #                         return True
                    # elif prev != i:
                        # return True
                # return false
    #             colors[cur] =2
    #             return False
        visited = [False] * V    
        def isCycleUtil(cur, parent):
            visited[cur] = True    
            for node in adj[cur]:
                if not visited[node]:
                    if isCycleUtil(node, cur):
                        return True
                elif parent != node:
                    return True
            return False    
            
        
        for v in range(V):
            if not visited[v]:
                if isCycleUtil( v, -1):
                    return 1
        return 0