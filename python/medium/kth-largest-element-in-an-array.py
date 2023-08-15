class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-n for n in nums]
        heapq.heapify(heap)

        res = 0
        while k:
            res = heapq.heappop(heap)
            k -= 1
        return res * -1
            
            
