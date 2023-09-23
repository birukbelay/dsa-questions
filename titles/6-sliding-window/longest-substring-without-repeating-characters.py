class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        d={}
        tot=0
        L=0
        long=0
        for i in range(len(s)):
            tot+=1
            print("tot-=", tot)
            c=s[i]
            if c in d:      
                # print("d=",d, "ttt-", tot)
                sub=d[c]-L+1
                print(sub)
                tot-=sub
                # print("tt==",tot)
                L=d[c]+1
                m=min(d, key=d.get)
                while m!=c:
                    d.pop(m,None)
                    m=min(d, key=d.get)
                # print("i-",i,"l-",l, "t-",tot,"lon", long)
                d[c]=i
            else:
                d[c]=i
            long=max(long, tot)
        return long