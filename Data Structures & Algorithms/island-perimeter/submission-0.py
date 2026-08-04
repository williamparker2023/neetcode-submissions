class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue

                curP = 0
                if (j>0 and grid[i][j-1] == 0) or j==0:
                    curP += 1
                if (j<n-1 and grid[i][j+1] == 0) or j==n-1:
                    curP += 1
                if (i>0 and grid[i-1][j] == 0) or i==0:
                    curP += 1
                if (i<m-1 and grid[i+1][j] == 0) or i==m-1:
                    curP += 1
                
                ans += curP
        return ans