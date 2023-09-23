class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        l=0
        stN=str(num)
        ctr=0
        for i in range(len(stN)):
            
            if i-l>=k-1:                
                new=int(stN[l:i+1])
                print(new, l,i)
                if new==0:
                    l+=1
                    continue
                if num%new ==0:
                    ctr+=1                   
                
                l+=1
        return ctr
