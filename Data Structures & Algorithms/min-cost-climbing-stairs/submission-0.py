class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return cost[0]
        if len(cost) == 2:
            return min(cost)
        
        prev1 = 0
        prev2 = 0
        n = len(cost)

        for i in range(2,n+1):
            cur = min(prev1 + cost[i-1], prev2 + cost[i-2])
            prev2 = prev1
            prev1 = cur
        return prev1 