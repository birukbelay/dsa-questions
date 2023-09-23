def collatz(n):
    if n==1:        
        return
    elif n%2==1:
        print("odd", n)
        n=n*3 +1
        print(n, end=',')
        collatz(n)
    else:
        n=n/2
        print(n, end=',')
        collatz(n)
        
collatz(3)  

# it fails