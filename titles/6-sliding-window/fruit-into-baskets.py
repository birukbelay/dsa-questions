# https://leetcode.com/problems/fruit-into-baskets/submissions/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l=0
        tot=0
        leng=0
        d = {}
        fN=0
        
        for i in range(len(fruits)):
            leng+=1
            
            d[fruits[i]]=i
            
            # print("d-",d)
            # print("len-", leng)
            if len(d)>2:  
                m=min(d, key=d.get)
                # print("m-",m)
                # print("tot=", tot, leng)
                leng-=d[m]-l+1
                # print(leng)
                l=d[m] +1               
                d.pop(m, None)
            tot=max(tot,leng)
        return tot
                
                

        
        
        
        
        
        
        
    def wrongFunction(self, fruits: List[int]):
        d={}
        f1=None
        f2=None
        for f in fruits:
            # print(f, d)
            if f in d:
                print("--",f)
                d[f]+=1
                
                if f!=f1 and d[f]>d[f1]:
                    f2=f1
                    f1=f
                
            else:
                print("n--",f)
                d[f]=1
                if f1==None:
                    f1=f
                elif f2==None:
                    f2=f
                # if d[f]>f1:
                #     f1=f
                # elif d[f]>f2:
                #     f2=f
        # print("f1=", f1,  "f2,",f2)
        # print("d-",d)
        return d[f1] +d[f2]
                
