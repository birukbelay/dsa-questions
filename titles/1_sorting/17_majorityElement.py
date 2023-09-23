def majorityElement(nums: list[int]) -> list[int]:
    num = len(nums)
    dict={}
    arr=[]
    for i in range(num):
        if nums[i] in dict:
            dict[nums[i]]=dict[nums[i]]+1
        else:
           dict[nums[i]]=1
    for key in dict:
        if dict[key]> num/3:
            arr.append(key)
    return arr
print(majorityElement([3,2,3]))
print(majorityElement([1,2]))
print(majorityElement([1]))