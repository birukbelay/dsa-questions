# https://leetcode.com/problems/powx-n/
class Solution:
    def myPow(self, x: float, n: int) -> float:        

        return self.xpow(x, n, x, abs(n))
    def xpow(self, x:float, n:int, tot:float, ctrN:int):
        if n==0:
            return 1
        if ctrN==1:
            if n<0:
                return 1/tot
            return tot
        if ctrN%2==0:
            return self.xpow(x*x, n, tot*x, ctrN/2)
        # print("x-",x, "n-",n)
        return self.xpow(x, n, tot*x, ctrN-1)