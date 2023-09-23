class Solution {
    
    public List<Integer> partitionLabels(String s) {
        ArrayList<Integer> output = new ArrayList<Integer>();
        HashMap<Character, Integer> letters = new HashMap<Character, Integer>();
         for (int i = 0; i < s.length(); i++) {
            letters.put(s.charAt(i), i);         
         }
         int l=0;
         int end=0;
        for(int i=0; i< s.length();i++){
            end=Math.max(end, letters.get(s.charAt(i)));
            if(end==i){
                output.add(i+1-l);
                l=i+1;;
            }
        }
        return output;



    }
}