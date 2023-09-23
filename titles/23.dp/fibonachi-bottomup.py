def fib(self, n: int) -> int:
       # State space representation
    prev, curr = 0, 1
    
    # Fill the dp table
    for num in range(2, n + 1):
        temp = prev + curr
        prev = curr
        curr = temp
    
    # Extract our answer
    return curr
