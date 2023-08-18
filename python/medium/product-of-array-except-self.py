class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixMult, postfixMult = [1] * (len(nums) + 1), [1] * (len(nums) + 1)

        for i in range(1, len(prefixMult)):
            prefixMult[i] = nums[i-1] * prefixMult[i-1]
            postfixMult[-i-1] = nums[-i] * postfixMult[-i] 
        res = [0] * len(nums)

        for i in range(len(nums)):
            res[i] = prefixMult[i] * postfixMult[i+1]
        return res
            
