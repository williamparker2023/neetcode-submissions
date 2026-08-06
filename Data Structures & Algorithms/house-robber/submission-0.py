class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        prev1 = max(nums[0],nums[1])
        prev2 = nums[0]
        n = len(nums)

        for i in range(2,n):
            cur = max(nums[i]+prev2,prev1)
            prev2 = prev1
            prev1 = cur
        
        return prev1