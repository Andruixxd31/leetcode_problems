class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        min_val = math.inf
        while l < r:
            m = (l + r) // 2
            min_val = min(min_val, nums[m])
            
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
        
        return min(min_val, nums[l])
