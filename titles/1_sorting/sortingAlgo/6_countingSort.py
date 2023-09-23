

def countingSort(arr):
    list1 =[0] *100
    for i in range(len(arr)):
        num = arr[i]
        list1[num]=list1[num]+1
    return list1


print(countingSort([2,1,9,3,3,4,5,6]))

