class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms = set()

        def dfs(cur,left):
            if len(left) == 0:
                perms.add(tuple(cur))
                return
            for i in range(len(left)):
                dfs(cur + [left[i]],left[:i] + left[i+1:])
        
        ans = []
        dfs([],nums)
        for perm in perms:
            ans.append(list(perm))
        return ans