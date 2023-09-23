# https://codeforces.com/gym/437545/problem/D
import sys
input = sys.stdin.readline
# from collections import Counter


n,d = [int(a) for a in input().split()]
class back():
    def __init__(self):
        self.flag=sys.maxsize
        self.visited=set()
    #  return sum  
    def d3(self, n):
        arr=list(str(n))
        s=sum([int(a) for a in arr])
        if len(str(s))==1:
            return s
        else:
            return self.d3(s)
    
    def soln(self, n, d, c, side):
        
        # //print(">>>>>>>>",n,d, "-------", c,"side-", side)
        if d in self.visited:
            return
        
        v2=self.d3(d)
        if n==d:
            #// print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            self.flag=c
            # print("flag=>>", sflag)
            return c
        self.visited.add(d)
        if n>d:
            return
        
        if d%2==0:
            self.soln(n, d//2, c+1, 2)
        
        #// print("v2--",v2)
        if v2%3==0:
            self.soln(n, d//3, c+1,3)
    def go(self,n,d):
        
        self.soln(n,d,0,0)
        if self.flag==sys.maxsize:
            print(-1)
        else:
            print(self.flag)

clss=back()   
clss.go(n,d)

# soln(120, 51840, 0,0)
# print("flag=", flag)
# if flag==0:
#     print(-1)
# else:
#     print(flag)