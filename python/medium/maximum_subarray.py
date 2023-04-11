class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        maxTotal = nums[0]
        for num in nums:
            total += num
            maxTotal = max(maxTotal, total)
            total = 0 if total < 0 else total
        return maxTotal
        
