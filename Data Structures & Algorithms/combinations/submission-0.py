class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        options = [(i+1) for i in range(n)]
        
        def dfs(cur, i):
            if len(cur) >= k:
                ans.append(cur)
                return
            if i >= n:
                return
            dfs(cur,i+1)
            dfs(cur + [options[i]], i+1)
        dfs([],0)
        return ans