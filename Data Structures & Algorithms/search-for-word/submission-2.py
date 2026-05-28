class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i,j,left):
            if len(left)==0:
                return True
            if i<0 or j<0 or i>=len(board) or j>=len(board[i]) or board[i][j]!=left[0]:
                return False
            temp = board[i][j]
            board[i][j] = "-1"
            try1 = dfs(i+1,j,left[1:])
            try2 = dfs(i-1,j,left[1:])
            try3 = dfs(i,j+1,left[1:])
            try4 = dfs(i,j-1,left[1:])
            board[i][j] = temp
            return try1 or try2 or try3 or try4

        for i in range(len(board)):
            for j in range(len(board[i])):
                if dfs(i,j,word):
                    print(i,j)
                    return True
        return False