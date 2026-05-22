class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        t = 0
        q = deque()
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i,j))
        
        size = len(q)
        while len(q)>0:
            print(q)
            if size == 0:
                t+=1
                size = len(q)
            size -=1
            

            temp = q.popleft()
            i = temp[0]
            j = temp[1]
            
            if i-1>=0:
                if grid[i-1][j] == 1:
                    grid[i-1][j] = 2
                    q.append((i-1,j))
            if i+1<n:
                if grid[i+1][j] == 1:
                    grid[i+1][j] = 2
                    q.append((i+1,j))
            if j-1>=0:
                if grid[i][j-1] == 1:
                    grid[i][j-1] = 2
                    q.append((i,j-1))
            if j+1<m:
                if grid[i][j+1] == 1:
                    grid[i][j+1] = 2
                    q.append((i,j+1))

            
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return t