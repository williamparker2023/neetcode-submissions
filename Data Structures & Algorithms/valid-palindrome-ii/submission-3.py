class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPal(st):
            l = 0
            r = len(st)-1
            while l<=r:
                if st[l] != st[r]:
                    return False
                l+=1
                r-=1
            return True
        
        l = 0
        r = len(s)-1
        while l<=r:
            if s[l]!=s[r]:
                return isPal(s[l:r]) or isPal(s[l+1:r+1])
            l+=1
            r-=1

        return True