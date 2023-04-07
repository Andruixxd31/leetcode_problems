class Solution(object):
    def containsDuplicate(self, nums):
        nums_unq = set()
        for n in nums:
            if n in nums_unq:
                return True
            nums_unq.add(n)
        return False
