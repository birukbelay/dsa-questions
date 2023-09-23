class ArrHeap:
    heapArray=[]
    def __init__(self) -> None:
        self.heapArray=[]
        
    def swap(self,index1, index2):
        # print(f'i1={index1}, i2={index2}, val1={self.heapArray[index1]}, val2={self.heapArray[index2]} ')
        # print("arr=", self.heapArray)
        self.heapArray[index1], self.heapArray[index2]= self.heapArray[index2],self.heapArray[index1]
        
    def getLeftChildIndex(self, index):
        return 2*index +1
    def getRightChildIndex(self, index):
        return 2*index +2
    def getParentIndex(self, index):
        if index==0:
            return 0
        return (index-1)//2  #this is because the index starts from one
    
    def correctUpwards(self, index):
        found=False        
        while not found:
            parentIndex=self.getParentIndex(index)
            # print("`````````````in while loop``````````````")
            # print(f'   i={index}, pI={parentIndex}, VI={self.heapArray[index]},  VpI={self.heapArray[parentIndex]}')
            if self.heapArray[index] < self.heapArray[parentIndex]:
                
                self.swap(index, self.getParentIndex(index))                
                index=self.getParentIndex(index)
                
            else:
                print("-->found, ending loop")
                found=True
    def insert(self, val):
        # print("->", val)
        self.heapArray.append(val)   
        
        curIndex=len(self.heapArray)-1
        self.correctUpwards(curIndex)    
        # print("inset", self.heapArray)

    def isValidIndex(self, index):
        return index>=0 and index<len(self.heapArray)
          
    def remove(self, index):
        # print(f'removing i={index}, val={self.heapArray[index]}')
        # print("array=", self.heapArray)
        self.swap(index, len(self.heapArray)-1)        
        self.heapArray.pop()
        # print("arrayAfterRemoval=", self.heapArray)
        self.correctUpwards(index)
        self.correctDownWard(index)
    def update(self, index, value):
        self.heapArray[index]=value
        self.correctUpwards(index)
        self.correctDownWard(index)
        
    def getSmallerChildIndex(self, index):
        if self.heapArray[self.getRightChildIndex(index)]< self.heapArray[ self.getLeftChildIndex(index)]:
            return self.getRightChildIndex(index)
        else:
            return self.getLeftChildIndex(index)
    
    def correctDownWard(self, index):
        # print("going down")
        # print(f'haveValidChildIndex={self.haveValidChildren(index)}, whichIsValid={self.whichIsValidIndex(index)} ')
        # print(f'vci={self.heapArray[self.whichIsValidIndex(index)]}, va={self.heapArray[index]} ')
        # print("arrDwn", self.heapArray)
        while self.haveValidChildren(index) and self.heapArray[self.whichIsValidIndex(index)] < self.heapArray[index]:
            # print(f'validIndex={self.whichIsValidIndex(index)}, index={index}')
            # print(f'swapping   i={index},child= {self.whichIsValidIndex(index)}')
            self.swap(self.whichIsValidIndex(index), index)
            
            # print("ha",self.heapArray)
            index=self.whichIsValidIndex(index)
        
    def haveValidChildren(self, index):
        return self.isValidIndex(self.getLeftChildIndex(index)) or self.isValidIndex(self.getRightChildIndex(index))
    def whichIsValidIndex(self, index):
        if self.isValidIndex(self.getLeftChildIndex(index)) and self.isValidIndex(self.getRightChildIndex(index)):
            return self.getSmallerChildIndex(index)
        elif self.isValidIndex(self.getLeftChildIndex(index)):
            return self.getLeftChildIndex(index)        
        else:
            return index
    
        
        
        
heap = ArrHeap()   

heap.insert(3)       
heap.insert(2)       
heap.insert(7)       
heap.insert(6)       
heap.insert(5)       
heap.insert(1)

heap.remove(1)       

