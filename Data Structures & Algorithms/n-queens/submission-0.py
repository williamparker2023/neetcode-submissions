class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []

        #curQueens is [x,y] of queens, m is number placed
        def dfs(curQueens,m):
            if m == n:
                ans.append(curQueens)
                return
            for i in range(n):
                if not curQueens:
                    dfs(curQueens + [[m,i]], m+1)
                    continue

                add = True
                for x,y in curQueens:
                    if i == y: #same row
                        add = False
                        break
                    elif i+m == x+y: #same NE diagonal
                        add = False
                        break
                    elif i + (n-m) == y + (n-x):
                        add = False
                        break
                if add:
                    dfs(curQueens + [[m,i]], m+1)
        dfs([],0)
        def toGrid(arr):
            temp = []
            for grid in arr:
                curr = ["."*n for _ in range(n)]
                for x,y in grid:
                    curr[y] = curr[y][:x] + "Q" + curr[y][x+1:]
                temp.append(curr)
            return temp
        return toGrid(ans)
                    