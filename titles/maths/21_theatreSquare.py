def theatreSquare(n,m ,k):
    
    row=0
    col= 0
    if n%k ==0:
        row= n//k
    else:
        row= n//k +1
        
    if m%k==0:
        col=m//k
    else:
        col=m//k +1
    print(col*row)
    

theatreSquare(1,1,1)