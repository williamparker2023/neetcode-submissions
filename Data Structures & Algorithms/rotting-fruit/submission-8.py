class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    q.append((i,j))
        
        mins = 0
        size = len(q)
        while q:
            if size<=0:
                size = len(q)
                mins+=1
            i,j = q.popleft()
            if i>0 and grid[i-1][j]==1:
                q.append((i-1,j))
                grid[i-1][j] = 2
            if i<len(grid)-1 and grid[i+1][j] == 1:
                q.append((i+1,j))
                grid[i+1][j] = 2
            if j>0 and grid[i][j-1] == 1:
                q.append((i,j-1))
                grid[i][j-1] = 2
            if j<len(grid[i])-1 and grid[i][j+1] == 1:
                q.append((i,j+1))
                grid[i][j+1] = 2
            size-=1
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        
        return mins