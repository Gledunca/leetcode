class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for i in range(n)] for i in range(m)]
        # print(grid)
        if m == 1 or n == 1:
            return 1
        for i in range(m):
            grid[i][-1] = 1
            print(grid)
        for i in range(n):
            grid[-1][i] = 1
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                grid[i][j] = grid[i][j+1] + grid[i+1][j]
        return grid[0][0]