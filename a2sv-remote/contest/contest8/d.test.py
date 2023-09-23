
def findIdx(s):
    temp={}
    last=0
    uniCtr=0
    for i, v in enumerate(s):
        
        if v in temp:
            # print(i,v, uniCtr)
            if uniCtr> 26:
                break
            else:
                print(i,v,  'd[v-',temp[v], "uql=",uniCtr, "lst=",last)
                last=max(last, temp[v]+1)
                temp[v]=i
                uniCtr = i-last
            
        else:
            if v!='?':
                temp[v]=i
        uniCtr+=1
        
    if uniCtr<26:
        # print(-1)
        return -1
    print(last, s[last:last+26])
    return last

print(findIdx("WELCOMETOCODEFORCESROUNDTHREEHUNDREDANDSEVENTYTWO"))