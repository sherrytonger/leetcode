__author__ = 'Sherry'
# Given a m x n grid filled with non-negative numbers, find a path from top
# left to bottom right which minimizes the sum of all numbers along its path.
# You can only move either down or right at any point in time.
class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    # def minPathSum(self, grid):
    #     if not grid:
    #         return 0
    #     m, n = len(grid[0]), len(grid)
    #     dp = [[float('inf')] * (m + 1) for i in range(n + 1)]
    #     dp[0][1], dp[1][0] = 0, 0
    #
    #     for i in range(1, n + 1):
    #         for j in range(1, m + 1):
    #             dp[i][j] = grid[i-1][j-1] + min(dp[i-1][j], dp[i][j-1])
    #     return dp[n][m]
    def minPathSum(self,grid):
        m = len(grid)
        n = len(grid[0])
        dp = [[float('inf')]*n for i in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1,m):
            dp[i][0] = dp[i-1][0]+grid[i][0]
        for j in range(1,n):
            dp[0][j] = dp[0][j-1]+grid[0][j]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]

        return dp[m-1][n-1]


sol = Solution()
print sol.minPathSum([[1,2,1],[3,4,1]])