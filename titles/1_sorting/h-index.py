# https://leetcode.com/problems/h-index/
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        l=len(citations)
        for i in range(l):
            if l-i<=citations[i]:
                return l-i
        return 0
        # if len(citations)==1:
        #     if citations[0]==0:return 0
        #     return 1
        # for i in range(1,l):
        #     if citations[l-i]<=i:
        #         return i-1
        # return l
        # for index, vit in enumerate(citations):
        #     if index>=vit:
        #         return index
        # return l
            
        # if len(citations)==1:
        #     if citations[0]==0:return 0
        #     return 1
        # cit=citations[(len(citations)-1)//2]
        # if cit==0:
        #     return 1
        # return cit