
def findOrignalArrFinal(changed):
    dict={}
    arr=[]
    changed.sort()
    for i in range(len(changed)):
        if changed[i] in dict:
            dict[changed[i]]=dict[changed[i]]+1
        else:
            dict[changed[i]]=1
    print("dict=",dict)
    for j in range(len(changed)):
        
        cur_key=changed[j]
        cur_VAL = dict[cur_key]       
        # needed=dict[cur_VAL*2]
         
        print("cur_Val=", cur_VAL,"curKey", cur_key)          
        if cur_VAL>0 and  cur_key*2 in dict and dict[cur_key*2]>0:
            # print("cur_Val=", cur_VAL,"dict[cur=", dict[cur_VAL*2])          
            
            dict[cur_key]=dict[cur_key]-1
            dict[cur_key*2]=dict[cur_key*2]-1
            if not dict[cur_key]  <0:                
                arr.append(cur_key)
    if len(arr)==len(changed)/2:
        return arr
    else:
        return []  


def findOriginalArrTry1(changed: list[int]) -> list[int]:
        changed.sort()
        num_dict=dict.fromkeys(changed, 0)
        
        print(num_dict)
        arr=[] 
        ctr=0
        for i in range(len(changed)):
            if i*2 in num_dict and i/2 not in arr:
                arr.append(i)
                ctr+=1
            if ctr>= len(changed)/2:
                return arr
        return arr
              
# print(findOriginalArrayN([1,3,3,4,2,6,8]))


def findOrgTry2(changed):
    changed.sort()  
    num_dict={}
    
    arr=[]
    lastIndex=1
    
    for i in range(len(changed)):
        try:
            if lastIndex<=i:
                lastIndex=i+1
            val=changed.index(changed[i]*2, lastIndex)
            print("i=", i,"val=", val)
            print("changed[i]=", changed[i],"changd[val=", changed[val])
            print("numDict", num_dict)
            
            # marking the index
            if not i in num_dict and  not val in num_dict:
                
                num_dict[i]=1
                num_dict[val]=1
                arr.append(changed[i])
                lastIndex=val
                print("---", "arr=", arr)
                print("")
                
        except:
            pass       
        #  if i*2 in changed:
    if len(arr)==len(changed)/2:
        return arr
    else:
        return []
     
        
# print(findOrg2([1,3,4,2,6,8]))
# print(findOrg2([6,3,0,1]))
 

def findOrignalArrayByDeleteTry3(changed: list[int]) -> list[int]: 
    
    i=0
    arr=[]
    changed.sort()
    while len(changed)>0 and i< len(changed)-1 :
        
        if changed[i]*2 in changed:
            try:
                val=changed[i]
                changed.remove(val *2)
                changed.remove(val)
                arr.append(val)
            except:
                return []
        
        else:
            i+=1
    if len(changed)==0:
        return arr
    else:
        return []
    
# print(findOrignalArray([4,2,0]))
# print(findOrignalArray([4,4,16,20,8,8,2,10]))
# print(findOrignalArray([0]))
# print(findOrignalArray([6,3,0]))
# print(findOrignalArray([1,3,4,2,6,8]))


def findOrignalOptTry4(changed):
    dict={}
    arr=[]
    changed.sort()
    for i in range(len(changed)):
        if changed[i] in dict:
            dict[changed[i]]=dict[changed[i]]+1
        else:
            dict[changed[i]]=1
    for key in dict:
        cur_VAL = dict[key]
        
        while dict[key] >0:            
            if key*2 in dict and dict[key*2] >0:
                arr.append(key)
                dict[key]=dict[key]-1
                dict[key*2]=dict[key*2]-1
    if len(arr)==len(changed)/2:
        return arr
    else:
        return []
    
        
            
            
    # print(dict)
    
# print(findOrignalOpt([4,2,0]))
# print(findOrignalOpt([4,4,16,20,8,8,2,10]))
# print(findOrignalOpt([0]))
# print(findOrignalOpt([6,3,0]))
print(findOrignalArr([6,3,0,1]))    
print(findOrignalArr([0,0,0,0]))    
# print(findOrignalArr([1,3,4,2,6,8]))    
# findOrignalOpt([4,4,16,20,8,8,2,10])

[1,3,4,2,6,8]