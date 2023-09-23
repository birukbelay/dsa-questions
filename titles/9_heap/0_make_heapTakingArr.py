

class ArrHeap:
    heapArray=[]
    def __init__(self) -> None:
        self.heapArray=[]
    def buildHeap(self,arr,n):
        print("arrBef=",arr)
        for i in range(n):
            self.heapify(arr, n, i)
            self.correctUpwards(arr, i)

    def heapify(self, arr,n, index):
        # print("heapifying***")
        self.correctUpwards(arr, index)
        self.correctDownWard(arr, index)
        
     
      
    def HeapSort(self, arr, n):
        # print("arrToBeSOrted=", arr)             
        self.buildHeap(arr,n)
        
        # print(f"arry bfr swap+++++++++",arr)
        self.swap(arr, 0, len(arr)-1)
        # print(f"arry bfr hepfy+++++++++",arr)
        self.heapify(arr[:-1], len(arr)-1, 0)
        # print(f"after hepfy+++++++++",arr)
        for i in range(1,n):

            j= -1*i
            # swap the (array, 0th element, arr.length-1-i)
            self.swap(arr[:j], 0, (len(arr)-i)-1)            
            self.heapify(arr[:j], len(arr)-i, 0)
        # print("sortedArr=", arr)
        
      
    def getLeftChildIndex(self, index):
        return 2*index +1
    def getRightChildIndex(self, index):
        return 2*index +2
    def getParentIndex(self, index):
        if index==0:
            return 0
        return (index-1)//2  #this is because the index starts from one
    
    def correctUpwards(self,arr, index):
        print(f'correctingUP--{index}|||')
        found=False        
        while not found:
            parentIndex=self.getParentIndex(index)
            # print("`````````````in while loop``````````````")
            # print(f'   i={index}, pI={parentIndex}, VI={self.heapArray[index]},  VpI={self.heapArray[parentIndex]}')
            if parentIndex>=0 and arr[index] < arr [parentIndex]:
                # print("notFound-->")
                self.swap(arr, index, self.getParentIndex(index))                
                index=parentIndex
                # print("arrAfter=", self.heapArray)
            else:
                print("-->found, ending loop")
                found=True
    def insert(self,arr, val):
        print("->", val)
        arr.append(val)   
        
        curIndex=len(arr)-1
        self.correctUpwards(arr, curIndex)    
        # print("inset",arr)

    def isValidIndex(self,arr, index):
        return index>=0 and index<len(arr)
          
    def remove(self,arr, index):
        # print(f'removing i={index}, val={self.heapArray[index]}')
        # print("array=", self.heapArray)
        self.swap(arr, index, len(self.heapArray)-1)        
        arr.pop()
        # print("arrayAfterRemoval=", arr)
        self.heapify(arr, index)
        
    def update(self, arr, index, value):
        arr[index]=value
        self.heapify(arr, index)
    
    
    def swap(self, arr, index1, index2):
        # print(f"bfrS-- i1={index1}, i2={index2}, arr={arr}")
        arr[index1], arr[index2]= arr[index2], arr[index1]
        # print(f'swap==> arr={arr}, i1={index1}, i2={index2}')          
    def getSmallerChildIndex(self, arr, index):
        if self.bothHaveValidIndex(arr, index):
            if arr[self.getRightChildIndex(index)]< arr[ self.getLeftChildIndex(index)]:
                return self.getRightChildIndex(index)
            else:
                return self.getLeftChildIndex(index)
        else:
            raise Exception("both don't have children")
    
    def correctDownWard(self,arr,  index):
        # print("going down")
        # print(f'correctingDown--{index}|||')
        # print(f'haveValidChildIndex={self.haveValidChildren(index)}, whichIsValid={self.whichIsValidIndex(index)} ')
        # print(f'vci={self.heapArray[self.whichIsValidIndex(index)]}, va={self.heapArray[index]} ')
        
        while self.haveValidChildren(arr, index) and arr[self.whichIsValidIndex(arr, index)] < arr[index]:
           
            cIndexToBeSwapped=self.whichIsValidIndex(arr, index)
            self.swap(arr, cIndexToBeSwapped, index)
            
            # print("ha",self.heapArray)
            index= cIndexToBeSwapped
        
    def haveValidChildren(self,arr, index):
        return self.isValidIndex(arr, self.getLeftChildIndex(index)) or self.isValidIndex(arr, self.getRightChildIndex(index))
    
    def whichIsValidIndex(self,arr, index):
        if self.bothHaveValidIndex(arr, index):
            return self.getSmallerChildIndex(arr, index)
        elif self.isValidIndex(arr, self.getLeftChildIndex(index)):
            return self.getLeftChildIndex(index)        
        else:
            return index
    
    def bothHaveValidIndex(self, arr, index):
        return self.isValidIndex(arr, self.getLeftChildIndex(index)) and self.isValidIndex(arr, self.getRightChildIndex(index))
           
        
        
heap = ArrHeap()   
arr1=[3,2,7,6,5,1]
heap.HeapSort(arr1, len(arr1))
# heap.insert(3)       
# heap.insert(2)       
# heap.insert(7)       
# heap.insert(6)       
# heap.insert(5)       
# heap.insert(1)

# heap.remove(1)       

