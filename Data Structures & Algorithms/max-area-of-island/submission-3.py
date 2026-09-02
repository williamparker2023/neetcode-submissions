class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
                return 0

            grid[i][j] = 0
            cur = 1
            cur += dfs(i+1,j)
            cur += dfs(i-1,j)
            cur += dfs(i,j+1)
            cur += dfs(i,j-1)        

            return cur
        
        big = 0
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                big = max(big, dfs(i,j))
        
        return big