class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def walk(i: int, j: int, areaCount: int) -> int:
            if i >= len(grid) or i < 0:
                return areaCount

            if j >= len(grid[0]) or j < 0:
                return areaCount

            if grid[i][j] == 0:
                return areaCount

            areaCount += 1

            grid[i][j] = 0
            areaCount = walk(i + 1, j, areaCount)
            areaCount = walk(i - 1, j, areaCount)
            areaCount = walk(i, j + 1, areaCount)
            areaCount = walk(i, j - 1, areaCount)

            return areaCount

        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxArea = max(walk(i, j, 0), maxArea)

        return maxArea
