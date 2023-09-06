class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = []
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)
        for p, s in cars:
            time = (target - p) / s
            if res:
                if time > res[-1]:
                    res.append(time)
            else:
                res.append(time)
        return len(res)
