from typing import List
from collections import defaultdict
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		
		def hasCycle(curNode, colors, prev):
		    # cycle found
		    if colors[curNode] == 2:
                return False
		    if colors[curNode] ==1:
		        return True
            colors[curNode] = 1
            
            for itm in adj[curNode]:
                if prev != itm:
                    found = hasCycle(itm, colors, curNode)
                    if found:
                        return True
            colors[curNode] = 2
            return False
        colors = [0] * V
        for i in range(v):
            
            found = hasCycle(i, colors, -1)
            if found:
                return True
            else:
                return False