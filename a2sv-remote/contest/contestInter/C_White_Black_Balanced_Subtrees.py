import sys
input = sys.stdin.readline
import threading
from collections import defaultdict



def main():
        
    t= int(input())
    for _ in range(t):

        n= int(input())
        arr = [int(a) for a in input().split()]
        s = input().strip()

        d=defaultdict(list)
        # build a tree
        for i, v in enumerate(arr):
            d[v].append(i+2)
        
        # global mainCtr=0

        def dfs(k):
            # nonlocal mainCtr
            curClr= s[k-1]

            b=0
            w=0
            if curClr=='W':
                w +=1
            else:
                b+=1
            
            if len(d[k])==0:
                return [b,w,0]
            t=0
            for itm in d[k]:
                res = dfs(itm)
                b+=res[0]
                w+=res[1]
                t+= res[2]
            if b==w:
                t +=1
            return [b,w, t]
        ans = dfs(1)
        print(ans[2])




sys.setrecursionlimit(1 << 30)

threading.stack_size(1 << 27)

main_thread = threading.Thread(target = main)

main_thread.start()

main_thread.join()