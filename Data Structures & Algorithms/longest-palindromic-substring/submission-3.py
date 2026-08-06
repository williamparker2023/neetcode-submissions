class Solution:
    def longestPalindrome(self, s: str) -> str:
        big = 0
        ans = [0,0]
        n = len(s)

        for i in range(n-1):
            l,r = i,i
            while l>=0 and r<n and s[l] == s[r]:
                if r-l > big:
                    big = r-l
                    ans = [l,r]
                l-=1
                r+=1
            l,r = i,i+1
            while l>=0 and r<n and s[l] == s[r]:
                if r-l > big:
                    big = r-l
                    ans = [l,r]
                l-=1
                r+=1
        
        return s[ans[0]:ans[1]+1]