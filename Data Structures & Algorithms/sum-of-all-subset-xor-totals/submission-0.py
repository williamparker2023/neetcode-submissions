class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = [0]
        nums = [0] + nums

        def dfs(i,cur):
            print(i,cur)
            
            if i>=len(nums)-1:
                return
            
            dfs(i+1,cur)
            ans[0] += cur ^ nums[i+1]
            dfs(i+1,cur ^ nums[i+1])
        dfs(0,0)
        return ans[0]