import sys
input = sys.stdin.readline
from collections import defaultdict, deque

t = int(input())
for _ in range(t):
    e = input()

    n, k = [int(a) for a in input().split()]
    d = defaultdict(list)
    ctr = defaultdict(int)
    ''' building the graph and the ctr '''
    for _ in range(n-1):
        u, v = [int(a) for a in input().split()]
        d[v].append(u)
        d[u].append(v)
        ctr[v] +=1
        ctr[u] +=1
    ''' adding the initial leaf nodes to the que '''
    que = deque()
    for key, v in ctr.items():
        if v==1:
            que.append(key)
    counter = 0
    nodeCtr=0
    ''' removing the leaf nodes using :level order traversal '''
    while que:
        if counter == k:
            break
        for i in range(len(que)):
            cur = que.popleft()
            nodeCtr +=1
            # ctr[cur]-=1
            ctr.pop(cur, None)
            for itm in d[cur]:
                ctr[itm] -=1
                if ctr[itm] ==1:
                    que.append(itm)
        counter +=1
        
    print(n-nodeCtr)
    # tot=0
    # ''' counting the remaining nodes '''
    # seen = set()
    # while que:
    #     for _ in range(len(que)):
    #         cur = que.popleft()
    #         ctr.pop(cur, None)
    #         # ctr[cur]-=1
    #         tot += 1
    #         for item in d[cur]:
    #             if ctr[item] > 1 and item not in seen:
    #                 que.append(item)
    #                 seen.add(item)
    #                 ctr[item] -=1
        

    
    # print(tot)
