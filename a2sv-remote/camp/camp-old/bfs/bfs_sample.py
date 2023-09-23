from collections import deque

def bfs(graph, start):
    visited = set()
    queue=deque([start])
    
    visited.add(start)
    while queue:
        current=queue.popleft()
        print(current)
        for neighbour in graph[current]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour  )
    