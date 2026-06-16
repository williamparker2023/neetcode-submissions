class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        pref = [nums[0]] + [0]*(n-1)

        for i in range(1,n):
            pref[i] = pref[i-1] + nums[i]
    
        smallestBefore =[0]*(n)
        for i in range(1,n):
            smallestBefore[i] = min(smallestBefore[i-1],pref[i-1])

        ans = -sys.maxsize
        for i in range(n):
            ans = max(ans, pref[i]-smallestBefore[i])
        
        print(pref)

        return ans