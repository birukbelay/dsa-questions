import sys
input = sys.stdin.readline
from collections import Counter


t= int(input())

for _ in range(t):
    n= int(input())
    arr = [a for a in input().strip()]

    stack =[]
    ans = 0
    for i in arr:
        if not stack:
            stack.append(i)
            continue
        if stack[-1]== i:
            stack.append(i)
            ans= max(ans, len(stack))
        else:
            stack.pop()
    print(max(ans+1,2))

    # ctr= Counter(arr)

    # great = '>'
    # less = '<'
    # ctr[great] = ctr.get(great, 0)
    # ctr[less] = ctr.get(less, 0)

    # ans = 0
    # diff = ctr[great]-ctr[less]
    # if diff==0:
    #     ans= ctr[less] +1
    # elif abs(diff)==1:
    #     ans = 2

    
    
