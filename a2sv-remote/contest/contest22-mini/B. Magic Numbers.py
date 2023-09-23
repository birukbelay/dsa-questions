import sys, threading

input = lambda: sys.stdin.readline().strip()


a =input()




def isMagic(a):
    l=len(a)-1
    while l>=0:
        
        if l>1:
            if a[l]=='4':
                if a[l-1]=='4':
                    if a[l-2] !='1':
                        return False
                    l-=2
                elif a[l-1]=='1':
                    l-=1
                else:
                    return False
            elif a[l]=='1':
                l-=1
            else:
                return False
        elif l==1:
            if a[l]=='1' or a[l]=='4':
                if a[l-1]=='1':
                    return True
                else:
                    return False
            else:
                return False
        elif l==0:
            return True if a[l]=='1' else False
                
        
if isMagic(a):
    print("YES")  
else:
    print("NO")
                
        
        
    
    

