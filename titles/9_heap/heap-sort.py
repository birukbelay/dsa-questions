getParent = lambda idx : 0 if idx<=0 else (idx-1)//2
getRightIdx = lambda idx:  2*idx +2
getLeftIdx = lambda idx: 2*idx +1

def getBigger(arr, n, i):
    big = i # Initialize the largest element as the root

    leftI = getLeftIdx(i)
    rightI = getRightIdx(i)

    # Check if the left child of the root exists and is greater than the root
    if leftI < n and arr[leftI] > arr[big]:
        big = leftI

    # Check if the right child of the root exists and is greater than the current largest element
    if rightI < n and arr[rightI] > arr[big]:
        big = rightI
    return big




class Solution:
    # Heapify function to maintain heap property.
    def heapify(self, arr, n, i):
        
        largest = getBigger(arr, n, i)       

        # Swap the root (i.e., largest element) if necessary and recursively heapify the affected sub-tree
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    # Function to build a Heap from array.
    def buildHeap(self, arr, n):
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

    # Function to sort an array using Heap Sort.
    def HeapSort(self, arr, n):
        self.buildHeap(arr, n)
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]  # Swap the root (max element) with the last element
            self.heapify(arr, i, 0)  # Heapify the reduced heap
            