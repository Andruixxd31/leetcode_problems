class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [stone * -1 for stone in stones]
        heapq.heapify(heap)
        while heap:
            if len(heap) == 1:
                return -1 * heap[0]

            y = heapq.heappop(heap)
            x = heapq.heappop(heap)
            if x != y: 
                heapq.heappush(heap, y - x)
        
        return 0
