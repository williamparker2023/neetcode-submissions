class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        smallest = prices[0]
        n = len(prices)

        for i in range(1,n):
            ans = max(ans, prices[i]-smallest)
            smallest = min(smallest, prices[i])
        return ans