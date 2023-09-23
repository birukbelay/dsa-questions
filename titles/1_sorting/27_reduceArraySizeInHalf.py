# https://leetcode.com/problems/reduce-array-size-to-the-half/

def minSetSize(arr: list[int]) -> int:
    dicn={}
    sum=0
    count=0
    for i in range(len(arr)):
        if arr[i] in dicn:
            dicn[arr[i]]=dicn[arr[i]]+1
        else:
            dicn[arr[i]]=1
    
    for w in sorted(dicn, key=dicn.get, reverse=True):
        sum+=dicn[w]
        count+=1
        print(w, dicn[w])
        if sum>=len(arr)/2:
            return count
        
        # 
    
# print(minSetSize([3,3,3,3,5,5,5,2,2,7]))   
print(minSetSize([1,9]))   
# d = {'one':1,'three':3,'five':5,'two':2,'four':4}
# a = sorted(d.items(), key=lambda x: x[1])    
# print(a)
# for w in sorted(d, key=d.get, reverse=True):
#     print(w, d[w])