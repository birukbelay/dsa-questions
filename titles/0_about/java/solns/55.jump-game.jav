class Solution {
    public boolean canJump(int[] nums) {
        int N= nums.length;
        int maxN = nums[0];
        
        if(N<2) return true;
        for (int i = 0; i < N; i++){
            maxN = Math.max(maxN, (i+nums[i]));
            if(i>=maxN){
                if(i==N-1) return true;
                return false;
            }
        }
        return true;
    }
}