# https://www.eolymp.com/en/submissions/13849448

import sys
input = sys.stdin.readline
from collections import defaultdict, deque

n,m  = [int(a) for a in input().split()]
d= defaultdict(list)

start, end  = [int(a) for a in input().split()]

for i in range(m):
    a, b  = [int(a) for a in input().split()]
    d[a].append(b)
    d[b].append(a)
def bfs():
    que = deque()
    que.append((start, [start]))
    visited= set()
    while que:
        cur = que.popleft()
        if cur[0]==end:
            return cur[1]
        if cur[0] not in visited:
            visited.add(cur[0])
            for i in d[cur[0]]:
                new= cur[1][:]
                new.append(i)
                que.append((i, new))

    return []
ans=bfs()
if len(ans):
    print(len(ans)-1)
    print(*ans)
else:
    print(-1)