class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo={}
        def dp(i,j):

            if i== len(triangle)-1:
                return triangle[i][j]
            
            if (i,j) in memo:
                return memo[(i,j)]
            # on index j
            ans1 = dp(i+1, j)

            # on index j+1
            ans2= dp(i+1, j+1)

            ans = min(ans1, ans2)
            ans += triangle[i][j]
            memo[(i,j)]= ans
            return ans
        return dp(0,0)

