# https://leetcode.com/problems/top-k-frequent-words/
import heapq
class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        dicn={}
        heapArr=[]
        newArr= []
        for i in words:
            if i in dicn:
                dicn[i]=dicn[i]+1
            else:
                dicn[i]=1
        
        for key, value in dicn.items():
            heapq.heappush(heapArr, (-value ,key))
        print("heapArr=",heapArr)
        for i in range(k):
            newArr.append(heapq.heappop(heapArr)[1])
                    
            
        
        return newArr