class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def helper(num, combs):
            if len(combs) == k:
                res.append(combs[:])
                return 
            
            for i in range(num, n+1):
                combs.append(i)
                helper(i + 1, combs)
                combs.pop()
        helper(1,[])
        return res
