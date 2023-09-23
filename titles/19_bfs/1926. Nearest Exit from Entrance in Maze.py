class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n,m=len(maze), len(maze[0])
        in_bound= lambda row, col: 0<=row <n and 0<=col<m
        DIR=[(0,1),(0,-1), (1, 0),(-1,0)]
        
        que= deque()
        que.append((entrance[0], entrance[1], 0))
        maze[entrance[0]][entrance[1]]='='
        minLen=sys.maxsize
        while que:
            
            cur = que.popleft()
            # print(cur)
            for i,j in DIR:

                px= cur[0]+i
                py= cur[1]+j
                
                if not in_bound(px, py) and cur[2]!=0:
                    minLen= min(minLen, cur[2])
                    # print("---",cur)
                    
                if in_bound(px, py) and maze[px][py]=='.':
                    maze[px][py]='='
                    que.append((px, py, cur[2]+1))
        if minLen==sys.maxsize:
            return -1
        return minLen
                    
            
            