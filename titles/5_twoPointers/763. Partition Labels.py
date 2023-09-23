# https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d={}
        output=[]
        for i in range(len(s)):
            d[s[i]]=i
        l=0
        end=0
        
        for i in range(len(s)):
            end = max(end,d[s[i]])
            
            if end==i:
                output.append(i+1-l)
                l=i+1
        return output
            
            
        