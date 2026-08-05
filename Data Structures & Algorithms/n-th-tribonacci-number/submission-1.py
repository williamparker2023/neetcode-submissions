class Solution:
    def tribonacci(self, n: int) -> int:
        prev1 = 1
        prev2 = 1
        prev3 = 0

        if n == 0:
            return 0

        for i in range(n-2):
            cur = prev3 + prev2 + prev1
            prev3 = prev2
            prev2 = prev1
            prev1 = cur
        
        return prev1