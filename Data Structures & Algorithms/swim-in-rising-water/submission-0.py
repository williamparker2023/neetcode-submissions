class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        def dfs(i,j,t):
            if i<0 or j<0 or i>=n or j>=n or (i,j) in visited or t<grid[i][j]:
                return False
            if i==n-1 and j==n-1:
                return True
            visited.add((i,j))
            north = dfs(i-1,j,t)
            south = dfs(i+1,j,t)
            east = dfs(i,j+1,t)
            west = dfs(i,j-1,t)
            return north or south or east or west

        n = len(grid)
        visited = set()
        for t in range(n**2):
            visited = set()
            if dfs(0,0,t):
                return t
        
        
        
        return -1