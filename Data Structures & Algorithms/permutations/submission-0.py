class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(curArr,leftArr):
            if len(leftArr) == 0:
                ans.append(curArr)
            for i in range(len(leftArr)):
                dfs(curArr + [leftArr[i]], leftArr[:i] + leftArr[i+1:])
        dfs([],nums)
        return ans