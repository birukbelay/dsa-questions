# Fast/Slow
# https://leetcode.com/problems/minimum-window-substring/
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        reqD={}
        dctr={}
        winLen=sys.maxsize
        w=(0,0)
        missing=len(t)        
        l=0
        for i in t:
            dctr[i]=0
            if i in reqD:
                reqD[i]+=1
            else:
                reqD[i]=1
        for r in range(len(s)):            
            i=s[r]
            # print("-",r)
            if i in reqD:            
                
                # print(">>>r-",r,i,"l-",l,s[l])
                # print("dctr-", dctr, "dreq-", reqD)
                
                if dctr[i]<reqD[i]:
                    missing-=1
                dctr[i]=dctr[i]+1
                # print(")---}",dctr)
                # print("miss-", missing)
            
            while missing<=0 and l<=r:
                
                newWin=r-l
                if newWin<winLen:
                    w=(l,r)
                    winLen=newWin
                # print("===win-", newWin, w)
                j=s[l]
                # print("--------------------",l,"-",j,  r,"-",i)                
                if s[l] in reqD:
                    dctr[j]-=1
                    if dctr[j]<reqD[j]:
                        missing+=1
                    # print(missing,")---}",dctr)
                l+=1
        # print("w-", w, winLen)
        if winLen==sys.maxsize:
            return ""
        return s[w[0]:w[1]+1]


        