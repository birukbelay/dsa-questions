def subsets( nums: List[int]) -> List[List[int]]:
    
    res=[]
    
    subset = []
    def dfs(i):
        if i>= len(nums):
            res.append(subset.copy())
            return
        
        # decision to include nums[i]
        subset.append(nums[i])
        dfs(i+1)
        
        #we donot include nums[i]
        subset.pop()
        dfs(i+1)
    dfs(0)
    res.sort()
    return res

def subsets(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        output = [[]]
        
        for i in nums:
            new = []
            for j in output:
                new.append(j + [i]  )            
            
            output += new
        
        return output      
        
        
        
 def subsets(self, nums: List[int]) -> List[List[int]]:
        
    lst=[]
    lst.append([])
    for i in range(len(nums)):
        lst.append([nums[i]])
        for j in range( i):
            lst.append([nums[j],nums[i]])
    return lst