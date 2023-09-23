
def compress(self, chars: List[str]) -> int:    
    walker, runner = 0, 0
    while runner < len(chars):
    
        chars[walker] = chars[runner]
        count = 1
        
        while runner + 1 < len(chars) and chars[runner] == chars[runner+1]:
            runner += 1
            count += 1
        
        if count > 1:
            for c in str(count):
                chars[walker+1] = c
                walker += 1
        
        runner += 1
        walker += 1
    
    return walker

        
    l=0
    ctr=0
    newArr=""
    for i in range(len(chars)):
        R=chars[i]
        L=chars[l]
        # while it is the same character
        if R==L:                
            ctr+=1
            # if it is the last character
            if i==len(chars)-1:
                # print("lst-i",i, newArr)
                newArr+=L
                s=str(ctr)                    
                for j in s:
                    if ctr!=1: newArr+=j
                
        else:
            if ctr>1:
                # print("--ctr", ctr)
                newArr+=L
                s=str(ctr)
                for j in s:
                    newArr+=j
                l=i
                ctr=1                    
                                    
            else:
                # print(",",ctr,newArr)
                newArr+=L
                l=i
                ctr=1
            if i==len(chars)-1:
                # print("lst-i",i,l, newArr)
                newArr+=chars[l]
                
    # s = [str(integer) for integer in newArr]
    # a = "".join(s)
    # print(newArr)
    for i in range(len(newArr)):
        chars[i]=newArr[i]
        
    # chars=newArr
    return len(newArr)