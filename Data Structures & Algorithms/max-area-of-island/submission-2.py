class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != 1:
                return 0
            grid[i][j] = 0
            u = dfs(i+1,j)
            d = dfs(i-1,j)
            r = dfs(i,j+1)
            l = dfs(i,j-1)
            return 1 + u + d + r + l
        
        big = 0
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    temp = dfs(i,j)
                    big = max(big,temp)
        
        return big