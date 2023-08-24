class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def walk(i: int, j: int):
            if i >= len(grid) or i < 0:
                return

            if j >= len(grid[0]) or j < 0:
                return

            if grid[i][j] == "0":
                return
            
            grid[i][j] = "0"
            walk(i + 1, j)
            walk(i - 1, j)
            walk(i, j + 1)
            walk(i, j - 1)

        amountIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    amountIslands += 1
                    walk(i, j)
        
        return amountIslands
