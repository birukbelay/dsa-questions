# https://leetcode.com/problems/top-k-frequent-elements/

def topKFrequent(nums: list[int], k: int) -> list[int]:
    dicn={}
    arr=[]
    count=0
    for i in range(len(nums)):
        if nums[i] in dicn:
            dicn[nums[i]]=dicn[nums[i]]+1
        else:
            dicn[nums[i]]=1
    print(dicn)
    for w in sorted(dicn, key=dicn.get, reverse=True):        
        count+=1
        arr.append(w)
        print(w, dicn[w], arr)
        if count>=k:
            return arr
        
print(topKFrequent([1,1,1,2,2,3], 2))