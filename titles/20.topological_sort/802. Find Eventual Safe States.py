class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        ans =[]
        que = deque()
        dependents = defaultdict(list)
        ctr = [0] * len(graph)
        for index, value in enumerate(graph):

            if len(value) ==0:
                que.append(index)
            else:
                ctr[index] = len(value)
                for item in value:
                    dependents[item].append(index)
        while que:
            item = que.popleft()
            ans.append(item)
            for dep in dependents[item]:
                ctr[dep] -=1
                if ctr[dep] == 0:
                    que.append(dep)
        ans.sort()
        return ans
        
                    



