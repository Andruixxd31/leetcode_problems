class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        subsets = []
        nums.sort()

        def helper(arr, i):
            if tuple(arr) in seen:
                return
            if i > len(nums) -1:
                subsets.append(arr[:])
                seen.add(tuple(arr))
                return
            
            arr.append(nums[i])
            helper(arr, i + 1)
            arr.pop()
            helper(arr, i + 1)
        
        helper([],0)
        return subsets
