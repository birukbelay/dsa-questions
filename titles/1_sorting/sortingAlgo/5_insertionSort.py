def insertionSortReverse(n, l):
    current= 0
     
                
            
         
insertionSortReverse(5, [1, 2, 8,5, 3])
# help(range) 

def insertionSort(leng,arr):
    for i in range(leng):
        ctr = leng-1
        # save num @ arr[ctr]
        num= arr[ctr]        
        while num < arr[ctr-1] and ctr>0:
            arr[ctr] = arr[ctr-1]
            ctr=ctr-1        
            print(arr)
        arr[ctr]= num
    print(arr)

insertionSort(5,[2, 4, 6, 8, 3])     
            
        