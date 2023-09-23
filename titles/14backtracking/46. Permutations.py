
def permute(nums: List[int]) -> List[List[int]]:
        
    result=[]

    # if it has only one number
    if len(nums)==1:            
        return [nums[:]]
    for i in range(len(nums)):
        
        n= nums.pop(0)
             
        perms = permute(nums)
        for per in perms:
            perm.append(n)
        result.extend(perms)
        nums.append(n)
    
    return result