class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        sieve = [True] * n
        sieve[0] = sieve[1] = False

        for i in range(2, math.ceil(math.sqrt(n))):
            if sieve[i]:
                for j in range(i * i, n, i):
                    sieve[j] = False

        return sum(sieve)
