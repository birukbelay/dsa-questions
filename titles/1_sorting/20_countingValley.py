def countingValley(s, path):
    print(path)
    valley=0
    prev_step=""
    step_ctr=0
    for i in range(s):
        if path[i] == 'U':
            step_ctr+=1
        elif path[i]=="D":
            step_ctr-=1
        if step_ctr==0 and path[i]=="U":
            valley+=1
        # print( "i=",i,"stepCtr=", step_ctr, path[i], "val=", valley  )
        prev_step==path[i]    
    return valley

print("count--->",countingValley(8, "UDDDUDUU"))
            
            
            
            
            
            
        
    