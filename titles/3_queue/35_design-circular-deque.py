# https://leetcode.com/problems/design-circular-deque/

class MyCircularDeques:
    maxCount=0
    deque=[]
    def __init__(self, k: int):
        self.maxCount=k
        self.deque=[]

    def insertFront(self, value: int) -> bool:
        if len(self.deque)>= self.maxCount:
            return False
        self.deque.insert(0,value)
        return True

    def insertLast(self, value: int) -> bool:
        if len(self.deque)>= self.maxCount:
            return False
        self.deque.append(value)
        return True

    def deleteFront(self) -> bool:
        if len(self.deque)== 0:
            return False
        self.deque.pop(0)
        return True

    def deleteLast(self) -> bool:
        if len(self.deque)== 0:
            return False
        self.deque.pop()
        return True

    def getFront(self) -> int:
        if len(self.deque)== 0:
            return -1
        
        return self.deque[0]

    def getRear(self) -> int:
        if len(self.deque)== 0:
            return -1
        
        return self.deque[-1]

    def isEmpty(self) -> bool:
        return len(self.deque)==0

    def isFull(self) -> bool:
        return len(self.deque)==self.maxCount
    
    
    
myCircularDeque =  MyCircularDeques(3)
myCircularDeque.insertLast(1);  #// return True
myCircularDeque.insertLast(2);  #// return True
myCircularDeque.insertFront(3); #// return True
myCircularDeque.insertFront(4); #// return False, the queue is full.
myCircularDeque.getRear();      #// return 2
myCircularDeque.isFull();       #// return True
myCircularDeque.deleteLast();   #// return True
myCircularDeque.insertFront(4); #// return True
myCircularDeque.getFront()