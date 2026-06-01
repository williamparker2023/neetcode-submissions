class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s) + [True]

        for i in range(len(s)-1,-1,-1):
            for word in wordDict:
                if i+len(word)>len(s):
                    continue
                if dp[i+len(word)] == True and s[i:i+len(word)] == word:
                    dp[i] = True

        return dp[0]