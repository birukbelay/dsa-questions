print("yo")
def smallest_num(nums):
    n= len(nums)
    arr=[None] * n
    for i in range(n):
        cnt=0
        for j in range(n):
            if nums[j]< nums[i]:
                cnt=cnt+1
        arr[i]=cnt
        # print("a->", arr)
    return arr
        
print(smallest_num([7,7,7,7]))
print(smallest_num([6,5,4, 4,8]))