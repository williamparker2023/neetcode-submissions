class Solution:
    def rob(self, nums: List[int]) -> int:
        #try 1:n and 0:n-1

        if len(nums)<=3:
            return max(nums)

        ans1 = 0
        ans2 = 0
        n = len(nums)

        prev1 = max(nums[1],nums[0])
        prev2 = nums[0]

        for i in range(2,n-1):
            cur = max(prev1,prev2 + nums[i])
            prev2 = prev1
            prev1 = cur
        
        ans1 = prev1

        prev1 = max(nums[2],nums[1])
        prev2 = nums[1]

        for i in range(3,n):
            cur = max(prev1,prev2 + nums[i])
            prev2 = prev1
            prev1 = cur
        
        ans2 = prev1
        
        return max(ans1,ans2)