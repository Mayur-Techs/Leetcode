from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        rows = len(grid)
        cols = len(grid[0])

        total = rows * cols

        k %= total

        # Step 1: Flatten the grid
        arr = []

        for row in grid:
            for num in row:
                arr.append(num)

        # Step 2: Rotate the array
        arr = arr[-k:] + arr[:-k]

        # Step 3: Convert back to 2D
        ans = []

        index = 0

        for i in range(rows):

            row = []

            for j in range(cols):
                row.append(arr[index])
                index += 1

            ans.append(row)

        return ans