from msilib import init_database


def bigV(n):
    j=n
    for i in range(n-1):
        print(" "*j,"\\", " "* ((n*2)-4), "/")  
        
        n=n-1
        j=j+1
    print(" "*j,"\\/")
    

# def pos(n):
#     if n<0:
#         return 0       
# # # print("."," "*4,"...")4


def bigV2(n):    
    for i in range(n-1):
        print(" "*i,"\\")  
        
        # n=n-1
        # j=j+1
    # print(" "*j,"\\/")
    
def bigV3(n): 
    # middle= " "   
    # middle_space= n*2 -4
    for i in range(n-1):
        print(" "*i,"\\")
        # print(" "*i,"\\", middle * middle_space, "/")
        # middle_space-=2     
# bigV3(8)


def bigV4(n):
    middle_space= n*2-2  
    
    for i in range(n):
        print(" " * i, "\\", " "* middle_space, "/")
        # print("*" * i, "\\", "@"* middle_space, "/")
        middle_space-=2
        
        
bigV4(5)
print("\\",  "/")