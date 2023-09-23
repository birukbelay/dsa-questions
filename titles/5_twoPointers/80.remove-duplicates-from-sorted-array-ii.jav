class Solution {
    public int removeDuplicates(int[] nums) {
        int N = nums.length;
        int len=2;
        if (N< len+1)
            return N;
        
        int st=len;
        for (var i=st; i<N; i++)
            if(nums[i]!=nums[st-len])
                nums[st++]=nums[i];         
        
        return st;
    }
}