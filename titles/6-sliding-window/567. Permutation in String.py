# https://leetcode.com/problems/permutation-in-string/
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2): return False
        
        win=len(s1)
        d1={}
        d2={}
        L=0        
        
        for i in range(len(s1)):
            d1[s1[i]]= 1+ d1.get(s1[i],0)          
            
        match=0

        for i in range(len(s2)):
            if match ==len(d1): return True
            r=s2[i]
            
            if r in d1:
                
                d2[r]= 1+ d2.get(r,0)
                # print("d2r",i,r,d2[r])
                if d2[r]==d1[r]: match+=1
                if d2[r]-1==d1[r] :match-=1
                    
            # print("--m",match) 
            # print(i, d1,d2)
            l=s2[L]            
            if i-L>=win:
                if l in d1:
                    # print("d2l",L,l,d2[l])
                    d2[l]-=1
                    if d2[l]==d1[l]: match+=1
                    if d2[l]+1==d1[l] :match-=1
                
                L+=1
        # print("m2", match,win)   
        if match ==len(d1): 
            return True 
        else: 
            return False
            
                

        
        