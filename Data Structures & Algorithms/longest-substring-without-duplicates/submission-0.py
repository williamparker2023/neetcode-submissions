class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        #letter to earliest ix
        dic = {}
        n = len(s)
        ans = 0

        while r<n:
            if s[r] in dic:
                ix = dic[s[r]]
                while l <= ix:
                    dic.pop(s[l])
                    l += 1
            dic[s[r]] = r
            
            r += 1
            ans = max(ans, r-l)
        return ans