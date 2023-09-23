class Solution:
    def countPrimes(self, n: int) -> int:
        if n<3:
            return 0
        is_prime: list[bool] = [True for _ in range(n)]
        is_prime[0] = is_prime[1] = False
        
        i = 2
        # we check untill square root bcs others are checked already by bottom numbers 
        while i * i < n:
            if is_prime[i]:
                # because bottom nums are already checked
                j = i * i # was j= 2 * i ()
                # filtering gout the non prime numbers
                while j < n:
                    is_prime[j] = False
                    j += i
            i += 1
        ctr=0
        for i in is_prime:
            if i:
                ctr+=1
        return ctr
