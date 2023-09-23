import sys
input = sys.stdin.readline
from collections import defaultdict

t = int(input())


for _ in range(t):
    epty = input()
    n, k = [int(a) for a in input().split()]
    friends = [int(a) for a in input().split()]

    rooms = [0]*(n+1)
    d=defaultdict(list)
    for _ in range(n-1):
        u, v = [int(a) for a in input().split()]
        d[u].append(v)
        d[v].append(u)

    # soln fing if friends can reach him
    # friends will visit all the room on one step then 

    for frnd in friends:
        rooms[frnd]=1
        for nxt in d[frnd]:
            rooms[nxt]=1
    def find(rooms):
        for room in d[1]:
            if rooms[room] ==0:
                return True
        return False
    if find(rooms):
        print("YES")
    else:
        print("NO")


