class Solution:

    def longestPalindrome(self, s: str) -> str:
        maxPal=1
        lft, rgt =0,0
        memo={}
        def dp(l,r):
            nonlocal maxPal, lft, rgt, memo
            if l<0 or r>=len(s):
                return 0           
            
            if s[l]==s[r]:
                if (r-l) +1>maxPal:
                    maxPal= (r-l) +1
                    # memo(l,r)=(r-l) +1
                    lft, rgt=l,r
                dp(l-1, r+1)

        for i in range(1, len(s)-1):
            dp(i-1, i+1)
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                dp(i, i+1)
        
        return s[lft:rgt+1]


s= Solution()

s.longestPalindrome("cbbd")