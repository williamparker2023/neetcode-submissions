class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(i,j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != 1:
                return 0
            grid[i][j] = 0
            tempArea = 1
            tempArea += dfs(i+1,j)
            tempArea += dfs(i-1,j)
            tempArea += dfs(i,j-1)
            tempArea += dfs(i,j+1)
            return tempArea
        
        ans = 0
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    temp = dfs(i,j)
                    ans = max(ans, temp)
        return ans