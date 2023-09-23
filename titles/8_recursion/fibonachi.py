
def fibonachi(n):
    if not str(n).isnumeric():
        print("not a number")
        return -1
    
    if int(n) <0  :
        return -1
    elif int(n)==0 :
        return 0
    elif int(n)==1:
        return 1
    else:
        return fibonachi(int(n)-1) + fibonachi(int(n)-2)
    

def getInput():
    number= input("inter the number:")
    val=fibonachi(number)
    
    if val==-1:
        print("your input needs to be a positive integer")
        getInput()
    else:
        print(val)
    


getInput()
        
# printu(fibonachi(6))