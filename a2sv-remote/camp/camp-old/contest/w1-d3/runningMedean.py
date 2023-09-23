# https://www.hackerrank.com/contests/a2sv3-contest-6/challenges/find-the-running-median
def median2(a, i):
    
    if i==0:
        return round(a[i] +0.0, 1)              
    if i%2==0:
        v=i//2
        med=(a[v] +a[v-1])/2   +0.0
        return round(med , 1)
    else:
        return a[i//2]
def median(a):
    i=len(a)
    
    if len(a)==1:
        return round(a[0] +0.0, 1)              
    if i%2==0:
        v=i//2
        med=(a[v] +a[v-1])/2   +0.0
        return round(med , 1)
    else:
        return a[i//2]
def runningMedian(a):
    # Write your code here
    newArr=[]
    for i in range(len(a)):
        newArr.append(a[i])
        newArr.sort()
        med=median(newArr)
        if i==0:
            print(  round(a[i] +0.0, 1))
        