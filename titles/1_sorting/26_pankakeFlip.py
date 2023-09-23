# https://leetcode.com/problems/pancake-sorting/


def checkArrEqual(arr1, arr2):
    
    for i  in range(len(arr1)):
        if (arr1[i] != arr2[i]):
            return False
    return True
                  
# print(checkArrEqual([3,2,1,4,0],[3,2,1,4,9]))
# print(checkArrEqual([0, 1, 2, 3, 4],[0, 3, 2, 1, 4]))

def findMaxIndex(arr):
    max=0
    for i in range(len(arr)):
        if arr[i]>arr[max]:
            max=i
    return max

def reverseArr(arr):
    end = len(arr)-1
    for i in range(len(arr)//2):
        arr[i], arr[end]=arr[end], arr[i]
        end-=1
    return arr   
# print(reverseArr([1,2,3,4,5,6]))
a=[1,2,3,4,5, 6]

# print(a[len(a):])
# print(a+[])
def pancakeSort(arr: list[int]) -> list[int]:
    print("0", arr)
    # the returned pancake arangement
    pankaceArr=[]
    # the last index
    lastIndex=len(arr)
    # the sorted arr
    orgArr=arr[:]
    sortedArr=arr[:]    
    workingArr=arr[:lastIndex]
    sortedArr.sort()
    
    print("1",arr,"2", sortedArr)
    
    s=3
    print("conditiov ====> " , checkArrEqual(sortedArr, arr))
    final=0
    while not checkArrEqual(sortedArr, arr) and final<len(orgArr)*2:
        print("=========>>>>>>>>>here, ```S==",final)
    #     # find the max value in the arr
        index = findMaxIndex(workingArr) 
        # the first arr to be reversed 
        arrToBeReversed=workingArr[0:index+1]
        print("index=", index, "indxdArrBefRevrs=", arrToBeReversed)
        reverseArr(arrToBeReversed)
        
        print("`--rvrsIndex=", arrToBeReversed, "-- endPartOfArr=",workingArr[index+1:])
        print("  ||||  concated the arrays and reversed them ||||")
        # concconcatinating the reversed part and the whole part
        concatArr=arrToBeReversed + workingArr[index+1:]
        # newArr == the Big Int reversed to last arr
        newArr=reverseArr(concatArr)       
        
        
        print("```````WholeReversedNewArr=", newArr)
        pankaceArr.append(index+1)
        pankaceArr.append(lastIndex)
        
        print("  ||||  finished the reverse and concat, decreasing the array scope ||||")
        
        
        print("```````lastIndex==", lastIndex)
        print("```````lenArr==",len(arr),'==>', arr)
        print("`````lst=", arr[lastIndex:])
        
        
        
        arr=newArr+arr[lastIndex:]
        lastIndex-=1
        workingArr=arr[:lastIndex]
        s+=1
        print("arr=", arr,"workingArr=",workingArr, "newArr", newArr)
        final+=1


    # print(sortedArr, arr)
    print("conditiov====>2", checkArrEqual(sortedArr, arr))
    return pankaceArr

print("-=>",pancakeSort([3,2,1,4,0]))
    
    
    # =============    DEPTECATED   =====================
    
def checkArrEqualWrongWay(arr1, arr2):
    dic={}
    for i in range(len(arr1)):
        if arr1[i] in dic:
            dic[arr1[i]]= dic[arr1[i]]+1
        else:
            dic[arr1[i]]=1
            
    for i in range(len(arr2)):
        if arr2[i] not in dic:
            print("2")
            return False
        if dic[arr2[i]]==0:
            print("1", arr2[i])
            return False
        dic[arr2[i]]= dic[arr2[i]]-1
    return True