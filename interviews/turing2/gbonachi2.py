
def gbonachi(n, x, y):
	if n==0: return x
	if n==1: return y
	return gbonachi(n-1, y, y-x)


# memo = {}
# def gboWithMemo(n, x, y):
#     if n==0:
#         return x
#     if n==1: 
#         return y
#     if (x,y) in memo:
#         return memo[(x,y)]
#     ans= gbonachi(n-1, y, y-x)
#     memo[(x,y)]=ans
#     return ans

def gibonacci(n, x, y):

    for i in range(n-1):
        temp=x
        x = y
        y = y-temp
    return y


def gibonacci3(n, x, y):
    '''
    return the nth gibonacci number with constant time
    '''
    gibonaccis = [x, y, y - x, -x, -y, x - y]
    return gibonaccis[n % 6]



print(gibonacci(5,0,1)==-1)
print(gibonacci(2,0,1)==1)
print(gibonacci(3,0,1)==0)
print(gibonacci(4,0,1)==-1)
print(gibonacci(5,0,1)==-1)
print(gibonacci(6,0,2)==0)