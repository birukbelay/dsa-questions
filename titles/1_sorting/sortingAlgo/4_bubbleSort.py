def bubbleSort(lists):
        
    for i, val1 in enumerate(lists):
        for j, val2 in enumerate(lists):
            if val2>lists[j]:
                lists[j-1], lists[j]= lists[j], lists[j-1]  
    return lists            
# the idea of buble sort is to  find the biggest one and take it to the end of the array
def bubbleSort2(lists):
    count=0        
    for i in range(len(lists)):
        # (i+1) is for not visiting the bubled up big ones
        for j in range(len(lists) - (i+1)):
            if lists[j]>lists[j+1]:
                lists[j+1], lists[j]= lists[j], lists[j+1] 
                count=count+1 
    print("Array is sorted in %s swaps" %(count))
    print("First Element:", lists[0])
    print("Last Element:", lists[-1])
    
    return count          
print("array is sorted in ",bubbleSort([19,65,23,90, 1]))  
print(bubbleSort2([19,65,23,90,2]))  
    
    
    