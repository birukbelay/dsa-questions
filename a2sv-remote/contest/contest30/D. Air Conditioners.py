import sys
input = sys.stdin.readline
# from collections import Counter

t = int(input())

for _ in range(t):
    epty = input()
    n, k = [int(a) for a in input().split()]
    apos = [int(a) for a in input().split()]
    temp = [int(a) for a in input().split()]

    ans = []
    for i in range(n):
        mi = sys.maxsize
        for j in range(k):
            cur = temp[j] + abs((i+1)- apos[j])
            mi = min(mi, cur)
        ans.append(mi)
    print(*ans)
