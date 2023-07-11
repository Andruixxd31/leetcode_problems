class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def helper(subset: List[int], jumps: int):
            if jumps > len(nums) -1:
                res.append(subset.copy())
                return

            subset.append(nums[jumps])
            helper(subset, jumps+1)
            
            subset.pop()
            helper(subset, jumps+1)   
        
        helper(subset, 0)
        return res
