# https://leetcode.com/problems/power-of-three/submissions/

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        # if n==0 :
        #     return False
        # elif n==1:
        #     return True
        # elif n%3!=0:
        #     return False
        # else:
        #     return self.isPowerOfThree(n/3)
        while n!=3 :            
            if n==0:
                return False
            elif n==1:
                return True                    
            if n%3!=0:
                return False
            else:
                n=n/3
        return True
            
            
        