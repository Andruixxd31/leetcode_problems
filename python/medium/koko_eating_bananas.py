class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def bananas(amount: int) -> bool:
            t = 0
            for bananas in piles:
                t += math.ceil(bananas/amount)
                if t > h:
                    return False

            return True 
        
        l, r = 1, 10 ** 9
        k = r
        while (l < r): 
            m = math.floor(l + (r - l)/2)
            if (bananas(m)):
                r = m
                k = m
            else:
                l = m + 1

        return k
