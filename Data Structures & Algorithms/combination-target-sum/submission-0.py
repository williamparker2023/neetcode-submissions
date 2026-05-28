class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ansSet = []
        nums.sort()

        def dfs(curNums,ix,curSum):
            if curSum == target:
                ansSet.append(curNums)
                return
            elif curSum>target:
                return
            for i in range(ix,len(nums)):
                dfs(curNums + [nums[i]], i, curSum + nums[i] )
        
        dfs([],0,0)
        return ansSet