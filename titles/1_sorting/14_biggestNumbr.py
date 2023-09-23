def concatNum(a,b):
    if str(a)+ str(b)> str(b) + str(a):
        return False
    return True
    


# def largestNumber(nums: list[int]):
    
#     nums= sorted(nums, cmp=concatNum)
#     return nums
    
# print(largestNumber([3,30,34,5,9]))     

def bubbleSort2(lists):      
    for i in range(len(lists)):
        for j in range(len(lists) - 1):
            if concatNum(lists[j], lists[j+1]):
                lists[j+1], lists[j]= lists[j], lists[j+1] 
                
    i= "".join(str(k) for k in lists)
    return i.lstrip('0')

print(bubbleSort2([3,30,34,5,9]))
            