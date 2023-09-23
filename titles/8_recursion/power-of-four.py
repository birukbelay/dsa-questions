# https://leetcode.com/problems/power-of-four/submissions/
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==0 :
            return False
        elif n==1:
            return True
        elif n%4!=0:
            return False
        else:
            return self.isPowerOfFour(n/4)
        # while n!=4 :            
        #     if n==0:
        #         return False
        #     elif n==1:
        #         return True                    
        #     if n%4!=0:
        #         return False
        #     else:
        #         n=n/4
        # return True