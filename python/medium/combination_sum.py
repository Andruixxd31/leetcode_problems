class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        permutation = []
        idx = 0

        def add_values(idx: int, total: int, permutation: List[int]): 
            if total >= target or idx >= len(candidates):
                if total == target:
                    res.append(permutation.copy())
                return
            
            permutation.append(candidates[idx])
            total += candidates[idx]
            add_values(idx, total, permutation)
            total -= permutation.pop()
            add_values(idx + 1, total, permutation)
        
        add_values(idx, 0, permutation)
        return res
