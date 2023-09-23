# answer for question on assignmnet II no.1
def palindrome(num):
    numStr=str(num)
    le=len(numStr)-1
    for i in range(len(numStr)//2):
        # print( i, numStr[i], numStr[le], le)
        if numStr[i]!=numStr[le]:
            return False
        le-=1
    return True


print(palindrome(123321))
palindrome(12321)


