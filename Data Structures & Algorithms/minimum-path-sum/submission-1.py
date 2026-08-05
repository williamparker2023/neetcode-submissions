class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        prev = [0]*n
        prev[0] = grid[0][0]
        for i in range(1,n):
            prev[i] = prev[i-1] + grid[0][i]
        dp = prev[:]

        for i in range(1,m):
            dp[0] = prev[0] + grid[i][0]
            for j in range(1,n):
                dp[j] = grid[i][j] + min(dp[j-1],prev[j])
            prev = dp[:]
        return dp[-1]