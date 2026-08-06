class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for _ in range(n)]

        if len(s) == 1:
            return s
        
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            return s[0]

        for i in range(n):
            dp[i][i] = True
        
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
        
        for i in range(1,n-1):
            l,r = i-1,i+1

            while l>=0 and r<n and s[l] == s[r]:
                dp[l][r] = True
                l-=1
                r+=1
            
            l,r = i-1,i

            while l>=0 and r<n and s[l] == s[r]:
                dp[l][r] = True
                l-=1
                r+=1

            l,r = i,i+1

            while l>=0 and r<n and s[l] == s[r]:
                dp[l][r] = True
                l-=1
                r+=1

        big = 0
        ans = ""
        for i in range(n):
            for j in range(i,n):
                if j-i > big and dp[i][j] == True:
                    big = j-i
                    ans = s[i:j+1]
        return ans