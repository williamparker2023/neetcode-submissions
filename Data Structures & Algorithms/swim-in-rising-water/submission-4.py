class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        def dfs(i,j,t):
            if i<0 or j<0 or i>=n or j>=n or (i,j) in visited or t<grid[i][j]:
                return False
            if i==n-1 and j==n-1:
                return True
            visited.add((i,j))

            return dfs(i-1,j,t) or dfs(i+1,j,t) or dfs(i,j+1,t) or dfs(i,j-1,t)

        n = len(grid)
        visited = set()
        l = 0
        r = n**2
        m = (l+r)//2
        ans = sys.maxsize
        while l<=r:
            m = (l+r)//2
            visited = set()
            if dfs(0,0,m):
                ans = m
                r = m-1
            else:
                l = m+1
        
        return ans