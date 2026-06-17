class Solution:
    def isPalindrome(self, s: str) -> bool:
        validLet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        validNum = "0123456789"
        n = len(s)
        l = 0
        r = n-1

        while l<r:
            if s[l] not in validLet and s[l] not in validNum:
                l += 1
            elif s[r] not in validLet and s[r] not in validNum:
                r -= 1
            elif s[l] in validLet and s[r] in validLet:
                if s[l].lower() == s[r].lower():
                    l += 1
                    r -= 1
                else:
                    return False
            elif s[r] in validNum and s[l] in validNum:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            else:
                return False
        return True