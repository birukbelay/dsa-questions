import sys
input = sys.stdin.readline
from collections import Counter


def main():
    n = int(input())
    count = Counter(list(map(int, input().split())))
    memo = {}

    def dp(i):
        if i in (0,1):
            return count[i]
        if i in memo:
            return memo[i]
        memo[i] = max(dp(i-1), dp(i-2) + count[i] *i)
        return memo[i]
    print(dp(max(count.keys())))


main()















def mains():

    # : -------  aproach 2
    n= int(input())
    arr = [int(a) for a in input().split()]
    ctr = Counter(arr)

    # ctr = {5: 5, 4: 5, 6: 4}
    sArr = sorted(ctr.items(), key= lambda item: (item[0] * item[1]), reverse=True)

    sDict = dict(sArr)

    tot =0


    for i, v in enumerate(sArr):
        keys = v[0]
        val = v[1]
        if keys in sDict:
            curSum = keys *val

            prev = sDict.get(keys-1, 0)
            nxt = sDict.get(keys +1, 0)

            sums = (prev * (keys-1)) +(nxt * (keys+1))

            if sums> curSum:
                # remove the cur val from dict & add its upper & lower values
                

                tot += sums
                sDict.pop(key, None)
                sDict.pop(key+1, None)
                sDict.pop(key-1, None)
            else:
                tot += curSum
                sDict.pop(keys, None)
                sDict.pop(keys+1, None)
                sDict.pop(keys-1, None)



    print(tot)
