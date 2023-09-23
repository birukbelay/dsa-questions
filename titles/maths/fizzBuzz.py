class Solution:
    def fizzBuzz(self, n:int):
        switch=True
        list=[]
         
        print("hello", n)
        
        return ["123"]
    
# print(Solution.fizzBuzz(0,3))

class Solution2:
    def fizzBuzz(self, n:int):
        list=[]
        x = range(6)
        for i in range(1, n+1):
            if(i%3==0 and i%5==0):
                list.append("FizzBuzz")
            elif (i%3==0):
                list.append("Fizz")
            elif (i%5==0):
                list.append("Buzz")
            else:
                list.append(str(i))
        return list
                
print(Solution2.fizzBuzz(0,20))
    