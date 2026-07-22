class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i,j,0))
        
        while q:
            i,j,dist = q.popleft()
            if i+1<m and grid[i+1][j] > dist+1:
                q.append((i+1,j,dist+1))
                grid[i+1][j] = dist+1
            if i-1>=0 and grid[i-1][j] > dist+1:
                q.append((i-1,j,dist+1))
                grid[i-1][j] = dist+1
            if j+1<n and grid[i][j+1] > dist+1:
                q.append((i,j+1,dist+1))
                grid[i][j+1] = dist+1
            if j-1>=0 and grid[i][j-1] > dist+1:
                q.append((i,j-1,dist+1))
                grid[i][j-1] = dist+1
        
