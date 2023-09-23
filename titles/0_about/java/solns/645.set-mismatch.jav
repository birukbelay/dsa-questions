class Solution {
    public int[] findErrorNums(int[] nums) {

        int N = nums.length;
        int[] duplicateList = new int[2];
        HashMap<Integer, Integer> allNums = new HashMap<Integer, Integer>();
        for (int i=0; i<N; i++){
            int k = nums[i];
            Integer j = Integer.valueOf(k);
            if(allNums.containsKey(j)){
                duplicateList[0]= k;
            }
            allNums.put(j, 1);          
             
        }
        // System.out.println(allNums);
        for (int i=1; i<N+1; i++){
            // int k = nums[i];
            // Integer j = Integer.valueOf(k);
           if(!allNums.containsKey(i)){
               System.out.println(i);
                duplicateList[1]=i;
            } 
        }
        return duplicateList;
    }
}