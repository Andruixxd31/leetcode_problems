class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        res = []
        for p in points:
            distance = (math.sqrt(math.pow(p[0],2) + math.pow(p[1],2)))
            distances.append([distance, p[0], p[1]])

        heapq.heapify(distances)

        while k:
            d, x, y = heapq.heappop(distances)
            res.append([x,y])
            k -= 1

        return res

