import sys
input = sys.stdin.readline
from collections import defaultdict

n= int(input())
d= defaultdict(list)
for _ in range(n-1):
    a, b = [int(a) for a in input().split()]
    d[a].append(b)
    d[b].append(a)

q= int(input())
def dfs(key, idx, query, seen):
    if idx== len(query)-1 and query[idx]==key:
        return True
    if idx>= len(query):
        return False
    val= query[idx]
    
    if key in seen and key != val:
        return False
    arr = d[val]
    if key ==val:
        idx+=1
    seen.add(key)
    ans = False
    for i in arr:
        ret = dfs(i, idx, query, seen)
        ans = ans or ret
    0000000000000000
    return ans

for _ in range(q):
    k = int(input())
    arr = [int(a) for a in input().split()]
    seen= set()
    ans = dfs(arr[0], 0, arr, seen)
    if ans:
        print("YES")
    else:
        print("NO")


