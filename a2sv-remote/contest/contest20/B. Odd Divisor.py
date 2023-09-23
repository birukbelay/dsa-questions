import sys
input = sys.stdin.readline
# from collections import Counter

n= int(input())

def hasOdd(x: int) -> bool:
    if x%2 !=0:
        return True
    d = 3
    # print("--",x)
    while d * 3 <= x:
        if x % d == 0 and d%2 !=0:
            return True
        d += 2
    return False
def soln(x: int) -> bool:
    if x%2 !=0:
        return True
    d = 3
    # print("--",x)
    while d * 3 <= x:
        if x % d == 0:
            return True
        elif x%2==0:
            x//=2
            continue
        d += 2
    return False
# print(soln(1099511627776))
for i in range(n):
    k= int(input())
    if soln(k):
        print('Yes')
    else:
        print("No")