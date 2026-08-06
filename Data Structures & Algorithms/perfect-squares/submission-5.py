class Solution:
    def numSquares(self, n: int) -> int:
        dp = [sys.maxsize]*(n+1)

        validSquares = set([i**2 for i in range(1,int(n**0.5)+1)])
        
        for i in range(1,n+1):
            if i in validSquares:
                dp[i] = 1
            for sq in validSquares:
                if i + sq > n:
                    continue
                dp[i+sq] = min(dp[i+sq],dp[i]+1)
        return dp[-1]