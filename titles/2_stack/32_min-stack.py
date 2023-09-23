# https://leetcode.com/problems/min-stack/


class MinStack:
    stack=[]
    minValues=[]
    min=0
    def __init__(self):
        self.stack=[]
        self.minValues=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minValues:
            self.minValues.append(val)
        elif val<self.minValues[-1]:
            # self.min=val
            self.minValues.append(val)
        

    def pop(self) -> None:
        topVal=self.stack.pop()
        if self.minValues:
            if topVal==self.minValues[-1]:
                self.minValues.pop()
            

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minValues[-1]
    

minStack = MinStack()
minStack.push(-2);
minStack.push(0);
minStack.push(-3);

print(minStack.getMin()); # return -3
print(minStack.pop())
print(minStack.top())   # // return 0
print(minStack.getMin()); #// return -2