class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        d=defaultdict(list)
        # create a pair array for each number
        for fr, to in edges:
            d[fr].append(to)
            
        print(d)
        reach= defaultdict(set)
        # make a dict with the reach of all the 
        def dfs(num, cur):
            if cur!=num:
                reach[num].add(cur)
            if cur in d:
                for i in d[cur]:
                    dfs(num, i)
        
        for k, v in d.items():
            dfs(k, k)
        ans=[]
        
        sort = sorted(reach.items(), key=lambda item: len(item[1]), reverse=True)
        
            
        print(sort)
        
        print(reach)
        # check which value contains all the other ones
        #start from longest & ignores the ones already in the array
        
        
        
        
        return ans