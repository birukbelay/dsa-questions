class Solution:
    def hammingWeight(self, n: int) -> int:
        
        #super optimized
        ctr=0
        while n:
            ctr+=1
            n= n& n-1
        return ctr
        
        ctr=0
        while n:
            if n% 2!=0:
                ctr+=1
            n = n>>1
        return ctr
        