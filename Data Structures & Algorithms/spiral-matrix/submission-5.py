class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #1:east,2:south,3:west,4:north
        dir = 0
        n = len(matrix)
        m = len(matrix[0])
        if m == 1:
            dir=1
        #right bottom left top
        bounds = [m-1,n-1,0,0]
        

        i,j = 0,0
        ans = [matrix[0][0]]
        if [ans] == matrix:
            return ans
        while True:
            if dir==0:
                j+=1
            elif dir==1:
                i+=1
            elif dir==2:
                j-=1
            else:
                i-=1
            ans.append(matrix[i][j])
            if (dir == 0 or dir == 2) and bounds[dir]==j:
                if dir==0:
                    bounds[3]+=1
                else:
                    bounds[1]-=1
                dir+=1
                dir%=4
            elif (dir == 1 or dir == 3) and bounds[dir]==i:
                if dir==1:
                    bounds[0]-=1
                else:
                    bounds[2]+=1
                dir+=1
                dir%=4
            if bounds[0]<bounds[2] or bounds[1]<bounds[3]:
                break
        return ans
