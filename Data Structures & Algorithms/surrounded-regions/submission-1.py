class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def isSurrounded(i,j):
            if i<0 or j<0 or i>=len(board) or j>=len(board[i]):
                return False
            if board[i][j] == "X":
                return True
            if i==0 or j==0 or i==len(board)-1 or j==len(board[i])-1:
                return False
            board[i][j] = "X"
            north = isSurrounded(i-1,j)
            east = isSurrounded(i,j+1)
            south = isSurrounded(i+1,j)
            west = isSurrounded(i,j-1)
            ans = north and east and south and west
            board[i][j] = "O"
            return ans

        def fillArea(i,j):
            if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or board[i][j]=="X":
                return
            board[i][j] = "X"
            fillArea(i+1,j)
            fillArea(i-1,j)
            fillArea(i,j+1)
            fillArea(i,j-1)
            return


        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                fill = isSurrounded(i,j)
                if fill:
                    fillArea(i,j)
        return