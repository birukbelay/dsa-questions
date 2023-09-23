
# 


def longestSubString(stringInput, k):
    
    bigestSum=0
    start=0
    dicn={}
    for i in range(len(stringInput)):
        schar=stringInput[i]
        if schar in dicn:
            dicn[schar]+=dicn[schar]+1
        else:
            dicn[schar]=1
            
        while len(dicn)>k:
            #TODO calculate total sum of integers
            
            del dicn[stringInput[start]]
            start+=1
        new_sum=0
        for value in dicn.values():
            new_sum+=value
        bigestSum=max(bigestSum, new_sum)
            
        