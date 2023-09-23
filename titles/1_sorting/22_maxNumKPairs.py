def maxOperations(nums: list[int], k: int) -> int:
        nums.sort()
        dict={}
        count=0
        print(nums)
        
        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]]=dict[nums[i]]+1
            else:
                dict[nums[i]]=1
               
        for i in range(len(nums)):
            n=nums[i]
            print("i=",i,"n=",n)
            if k-n in dict and dict[n]>0 and dict[k-n]>0:
                print("dict ==>",dict)
                print( "dict[n]=",dict[n],"k-n=", k-n,"dic->", dict[k-n])
                if  n== k-n and dict[n]==1:
                    continue
                count+=1
                dict[n]-=1
                # print(i,"=d-n",dict[n])
                dict[k-n]-=1
                # print(i,"=d-n",dict[k-n])
        return count
    
# print(maxOperations([3,1,3,4,3], 6))
print(maxOperations([1,2,3,4], 5))
                
                
                
                
            
            