# https://leetcode.com/problems/longest-nice-substring/submissions/

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        def dfs(string):
            hashset=set(string)
            if len(string)<2:
                return ""
            for i in range(len(string)):
                if not (string[i].lower() in hashset and string[i].upper() in hashset):
                    s1=dfs(string[:i])
                    s2=dfs(string[i+1:])
                    return s2 if len(s2)> len(s1) else s1
            return string
        return dfs(s)
        
#         d={}
#         v={}        
#         for i in s:
#             if i not in d:
#                 d[i]=0
                
#             if i.isupper():                
#                 if i.lower() in d:
#                     v[i]=0
#                     v[i.lower()]=0
#             else:
#                 if i.upper() in d:
#                     v[i]=0
#                     v[i.upper()]=0            
#         ctr=0
#         tot=0
#         l=0   
#         pl,pr=0,0
#         print(v)
#         for i in range(len(s)):
#             ctr+=1            
#             if s[i] not in v:
#                 ctr=0
#                 l=i+1
#             if ctr>=tot:
#                 tot=ctr
#                 pl,pr=l,i       
                
                
#         print(l,i)
#         print(s[l:i])
#         return s[l:i+1]
            
