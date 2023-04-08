class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        unq = set()
        swStart = 0
        for swEnd, num in enumerate(nums):
            if num in unq: 
                return True
            unq.add(num)
            if swEnd > k -1:
                unq.remove(nums[swStart])
                swStart += 1

        return False
            
