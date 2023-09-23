

def newYr(n,k):  
    total_contest_min= (4*60) -k
    contest_sum=0
    qstn_ctr=0   
    while contest_sum <= total_contest_min and qstn_ctr<=n:
        contest_sum += (qstn_ctr+1)*5
        qstn_ctr+=1
        print("tot", total_contest_min,"contest_sum,", contest_sum,  "ctr=", qstn_ctr)
         
    print(qstn_ctr-1)     
  
# n,k = map(int,input().split())   
# newYr(3, 222)
newYr(4, 190)

# input1 = input("")
# val=input1.split()
# k=int(val[1])
# n=(val[0])
        

def newYr(n,k):  
    total_contest_min= (4*60) -k
    contest_sum=0
    qstn_ctr=0   
    while contest_sum <= total_contest_min and qstn_ctr<=n:
        contest_sum += (qstn_ctr+1)*5
        qstn_ctr+=1
        
         
    print(qstn_ctr-1)     
  
n,k = map(int,input().split())   
newYr(n,k)