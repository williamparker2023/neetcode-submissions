class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.n = len(matrix)
        self.m = len(matrix[0])
        self.prefMat = [ [0] + [matrix[_][0]] + [0]*(self.m-1) for _ in range(self.n) ]
        self.prefMat = [[0]*(self.m+1)] + self.prefMat
        print(self.prefMat)
        for i in range(1,self.m+1):
            self.prefMat[1][i] = self.prefMat[1][i-1] + matrix[0][i-1]

        for i in range(1,self.n+1):
            for j in range(1,self.m+1):
                self.prefMat[i][j] = self.prefMat[i-1][j] + self.prefMat[i][j-1] - self.prefMat[i-1][j-1] + matrix[i-1][j-1]
        print(self.prefMat)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.prefMat[row2+1][col2+1] - self.prefMat[row2+1][col1] - self.prefMat[row1][col2+1] + self.prefMat[row1][col1]
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)