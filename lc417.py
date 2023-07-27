from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()

        def dfs(row, col, prevHeight, visited):
            if (row, col) in visited:
                return
            if (
                row < 0 or
                col < 0 or
                row >= len(heights) or
                col >= len(heights[0]) or
                prevHeight > heights[row][col]
            ):
                return
            visited.add((row, col))
            dfs(row-1, col, heights[row][col], visited)
            dfs(row, col+1, heights[row][col], visited)
            dfs(row+1, col, heights[row][col], visited)
            dfs(row, col-1, heights[row][col], visited)

        # Go along left and right columns, getting west pacific and east atlantic
        for i in range(len(heights)):
            dfs(i, 0, 0, pacific)
            dfs(i, len(heights[0])-1, 0, atlantic)

        # Go along top and bottom rows, getting north pacific and south atlantic
        for i in range(len(heights[0])):
            dfs(0, i, 0, pacific)
            dfs(len(heights)-1, i, 0, atlantic)

        return list(pacific.intersection(atlantic))