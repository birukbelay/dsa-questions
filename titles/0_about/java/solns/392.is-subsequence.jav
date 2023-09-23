class Solution {
    public boolean isSubsequence(String s, String t) {
        int l=0;
        int N = s.length();
        int M = t.length();
        if(N==0)
            return true;
        for (int i=0; i<N; i++){
            while(l< M && s.charAt(i)!=t.charAt(l)){
                l++;                
            }
            if(l==M){
                if(i!=N-1 || s.charAt(i)!=t.charAt(l-1))
                    return false;                
            }                
            if (s.charAt(i)==t.charAt(l)){
                if(i==N-1)
                    return true;
                l++;                
            }
        }
        return false;
    }
}