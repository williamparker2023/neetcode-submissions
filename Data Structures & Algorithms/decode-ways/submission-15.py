class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if s[0] == "0":
            return 0
        if n == 1:
            return 1
        

        dp = [0]*n
        dp[0] = 1
        if int(s[0:2]) <= 26 and s[1] != "0":
            dp[1] = 2
        elif (int(s[0:2]) <= 26 and s[1] == "0") or (int(s[0:2]) > 26 and s[1] != "0"): 
            dp[1] = 1
        elif s[1] == "0":
            return 0
        
        for i in range(2,n):
            if s[i] == "0" and (int(s[i-1])>=3 or int(s[i-1])==0):
                return 0
            elif int(s[i-1:i+1]) <= 26 and int(s[i-1:i+1]) >= 10 and s[i] != "0":
                dp[i] = dp[i-1] + dp[i-2]
            elif s[i] == "0":
                dp[i] = dp[i-2]
            else:
                dp[i] = dp[i-1]
        print(dp)
        return dp[-1]