getParent= lambda idx : 0 if idx==0 else (idx-1)//2
def getRightIdx(idx):
    return 2*idx +2
def getLeftIdx(idx):
    return 2*idx +1

class MinHeap:



    def heapify(self, arr,n, index):
        
        self.upHeap(arr, i)
        self.downHeap(arr, i)
    # given an array build the heap from it
    def buildHeap(self,arr,n):        
        # for each array position correct the value at that position
        for i in range(n):
            self.heapify(arr, n, i)
            self.upHeap(arr, i)





    # ------------  utility functions
    def swap(self, arr, l, r):
        arr[r], arr[l] =arr[l], arr[r]
        # check an index is valid
    def isValidIdx(self,arr, idx):
        return idx>=0 and idx<len(arr)
    def haveChilds(self,arr, idx):
        return self.isValidIdx(arr, getRightIdx(idx)) or self.isValidIdx(arr, getLeftIdx(idx))
    def getSmallChildIdx(self,arr, idx):
        if self.isValidIdx(arr, getLeftIdx(idx)) and self.isValidIdx(arr, getRightIdx(idx)):            
            return getLeftIdx(idx) if getLeftIdx(idx) < getRightIdx(idx) else  getRightIdx(idx)        
        return getLeftIdx(idx) if self.isValidIdx(arr, getLeftIdx(idx)) else idx 
    

    def upHeap(self,arr, idx):        
        while arr[getParent(idx)] > arr[idx]:
            self.swap(arr, idx, getParent(idx))            
            idx= getParent(idx)
    def downHeap(self,arr, idx):
        while self.haveChilds(arr, idx) and arr[self.getSmallChildIdx(arr, idx)] < arr[idx]:
            self.swap(arr, self.getSmallChildIdx(arr, idx), idx)
            idx= self.getSmallChildIdx(arr, idx)
   
    
    def remove(self,arr, idx):
        self.swap(arr, idx, len(arr)-1)
        arr.pop()
        self.upHeap(arr, idx)
        self.downHeap(arr, idx)
    #add a value to the heap
    def insert(self,arr, val):
        arr.append(val)
        self.upHeap(arr, len(arr)-1)
    # to updte the value of an element in the array & correct the heap
    def update(self, arr, idx, val):
        arr[idx]= val
        self.upHeap(arr, idx)
        self.downHeap(arr, idx)


