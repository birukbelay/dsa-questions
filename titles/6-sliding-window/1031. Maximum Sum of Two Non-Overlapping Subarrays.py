class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:


        # do a CDF(prefix sum) so that range sum can easily be calculated
        for i in range(1, len(A)):
            A[i] += A[i - 1]


        res, Lmax, Mmax = A[L + M - 1], A[L - 1], A[M - 1]


        # window  | --- L --- | --- M --- |
        for i in range(L + M, len(A)):
            Lmax = max(Lmax, A[i - M] - A[i - L - M]) #val @end of L-win - val @start of l-win
            mmax= A[i] - A[i - M]
            res = max(res, Lmax + mmax)

        # window  | --- M --- | --- L --- |
        for i in range(L + M, len(A)):
            Mmax = max(Mmax, A[i - L] - A[i - L - M])
            lmax = A[i] - A[i - L]
            res = max(res, Mmax + lmax)

        return res