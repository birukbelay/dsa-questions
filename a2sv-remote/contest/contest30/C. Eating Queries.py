import sys
input = sys.stdin.readline
# from collections import Counter

t = int(input())
for _ in range(t):

    n, q = [int(a) for a in input().split()]
    arr = [int(a) for a in input().split()]

    arr.sort(reverse=True)
    tot = sum(arr)
    # print("tot-", tot)
    for _ in range(q):
        c = int(input())
        # print("c-", c)

        if c>tot:
            print(-1)
        else:
            tots =0
            
            for i in range(len(arr)):
                tots += arr[i]
                if tots >=c:
                    print(i+1)
                    break
                

