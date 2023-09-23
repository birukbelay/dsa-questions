
def frequency(n, c):
    count=0
    while n>0:
        val=n%10
        n=n//10
        if val==c:
            count=count+1   
    return count

frequency(33344563, 3)