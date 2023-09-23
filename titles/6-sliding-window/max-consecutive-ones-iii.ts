// https://leetcode.com/problems/max-consecutive-ones-iii/submissions/
function longestOnes(nums: number[], k: number): number {
    let ks=k
    let l=0
    let tot=0
    let ctr=0
    for (let i = 0; i < nums.length; i++){
        
        
        if(nums[i]===0){            
            if(ks>=0) ks-=1
            // console.log("ks=",ks)
        }
        
        while(ks<0 && l<=i){
            if(nums[l]==0){                
                ks+=1                
            }
            l+=1
            ctr-=1
        }
        
        ctr+=1
        // console.log("i-", i, "crt=",ctr)
        tot=Math.max(tot, ctr)
    }
    return tot
};