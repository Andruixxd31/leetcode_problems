class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = []
        for i in range(len(temperatures)-1,-1,-1):
            while True:
                if stack and temperatures[i] >= stack[-1][0]:
                    stack.pop()
                else:
                    if stack:
                        res.append(stack[-1][1] - i)
                    else:
                        res.append(0)
                    stack.append([temperatures[i],i])
                    break
        res.reverse()
        return res
