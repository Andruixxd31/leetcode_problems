class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        rotated = []

        for row in boxGrid:
            empty = n - 1
            for i in reversed(range(n)):
                if row[i] == "*":
                    empty = i - 1
                elif row[i] == "#":
                    if i != empty:
                        row[empty], row[i] = row[i], "."
                    empty -= 1

        for i in range(n):
            new_row = []
            for j in range(m):
                new_row.append(boxGrid[m - 1 - j][i])
            rotated.append(new_row)
        return rotated
