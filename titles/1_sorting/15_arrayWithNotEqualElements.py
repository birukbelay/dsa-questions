# You are given a 0-indexed array nums of distinct integers.
# You want to rearrange the elements in the array such that
# every element in the rearranged array is not equal to 
# the average of its neighbors.
# https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/

def avg(x,y):
    return (x+y)/2

def rearrangeArray2( nums: list[int]) -> list[int]:
        for i in range(1, len(nums)-1):
            ctr=1
            while avg(nums[i-1], nums[i+1])==nums[i]:
                print("i=", i, "ctr=", ctr, 'len=', len(nums))
               
                nums[i], nums[i+ctr]= nums[i+ctr], nums[i]
                
                ctr=ctr+1
                print("i=", i, "ctr=", ctr, "nums=", nums)
        return nums        
    
    
# print(rearrangeArray([5,3,7,4,10]))
# print(rearrangeArray([1,2,3]))
print(7%2)
for i in range(7//2):
    print(i)
    
def rearrangeArray( nums: list[int]) -> list[int]:
    list2=[]
    nums.sort()
    i=0
    while i < len(nums)//2:
        list2.append(nums[i])
        list2.append(nums[len(nums)-i-1])
        i=i+1
    if len(nums)%2>0:
        list2.append(nums[i])
    return list2
print(rearrangeArray([1,2,3]))          
print(rearrangeArray([6,2,0,9,7]))
print(rearrangeArray([10,7,5,4,3]))
    # for i in range(len(nums)//2):
         
    
         