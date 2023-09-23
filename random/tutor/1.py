


def output1():
    rows=6
    string="python"
    for i in range(rows, 0, -1):
        j=0
        for k in string:
            if j==i:
                break
            print(j, end=k)
            j+=1
        print('')
    
output1()
def armstrong():
    digits=0  #count of length of number
    result=0  
    number=153
    number1=number #copy of number
    temp=number

    while number!=0:
        number= number//10
        digits+=1

    # print("number=", number, "num1=",number1, "temp=",temp)
    # print("digits", digits)

    while number1!=0:
        number=number1%10
        result=result+ number**digits
        number1=number1//10
    
    # print("number=", number, "num1=",number1, "temp=",temp)
    # print("result=",result)  
    if result==temp:
        print("number is armstrong")
    else:
        print("not")
        
        
# k="abebe"
# print(k[0:3:1])       
# for i in range(11,5):
#     print(i, end="")


# t1=[1,2,3,4,5,6,7,8]
# t2=[1,2,3,4]



# t3=t1+t2
# print(t3[0:12:3])



# data=[2,3,9]

# for x in range(3):
#     temp=[x for x in data]
#     print(temp)
    
    

    