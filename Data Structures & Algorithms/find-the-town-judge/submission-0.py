class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inOut = [[0,0] for _ in range(n+1)]
        
        for u,v in trust:
            inOut[u][1] += 1
            inOut[v][0] += 1
        

        for i in range(1,n+1):
            if inOut[i][0] == n-1 and inOut[i][1] == 0:
                return i
        return -1