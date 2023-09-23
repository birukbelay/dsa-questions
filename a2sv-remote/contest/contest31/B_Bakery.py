import sys
input = sys.stdin.readline
from collections import defaultdict

city = defaultdict(list)
n, m, k = [int(a) for a in input().split()]

for _ in range(m):
    u, v, l = [int(a) for a in input().split()]
    city[u].append([v, l])
    city[v].append([u, l])

if k > 0:
    arr = [int(a) for a in input().split()]
    stor = set(arr)

    minL = sys.maxsize

    for st in arr:        
        for ci, dis in city[st]:
            if ci in stor:
                continue
            minL = min(minL, dis)
    if minL == sys.maxsize:
        print(-1)
    else:
        print(minL)


else:
    print(-1)