class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def dfs(i,j,depth):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[i]) or grid[i][j]==-1 or (grid[i][j]==0 and depth!=0) or depth>grid[i][j]:
                return
            grid[i][j] = depth
            dfs(i+1,j,depth+1)
            dfs(i-1,j,depth+1)
            dfs(i,j+1,depth+1)
            dfs(i,j-1,depth+1)
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    dfs(i,j,0)
