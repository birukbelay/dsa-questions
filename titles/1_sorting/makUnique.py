def makeUnique(nums):
    d={}
    ctr=0    
    # d={3:1, 2:1, 1:1, 7:1}
    nums.sort()
    bigN=nums[0]
    for i in nums:
        c=i
        if c in d:
            dif=bigN+1-c
            ctr+=dif
            d[bigN+1]=1
            bigN+=1     
        if c not in d:
            d[c]=1
            bigN=c
    return ctr