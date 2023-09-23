



def minPairSum(nums: list[int]) -> int:
    nums.sort()
    
    arr=[]
    l=len(nums)-1
    for i in range(len(nums)//2):
        arr.append(nums[i]+nums[l])
        l-=1
    arr.sort()
    # print(max(arr))
    return max(arr)

# print(minPairSum([3,5,4,2,4,6]))
print(minPairSum([3,5,2,3]))