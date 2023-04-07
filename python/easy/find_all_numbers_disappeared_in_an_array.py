class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        uniq = set()
        res = []
        
        for val in nums:
            uniq.add(val)
        
        for i in range(1,len(nums)+1):
            if i not in uniq:
                res.append(i)
        return res
        
