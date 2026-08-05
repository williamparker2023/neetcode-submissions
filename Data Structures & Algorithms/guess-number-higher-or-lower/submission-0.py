# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 0
        r = n
        m = (l+r)//2

        while l<r:
            cur = guess(m)
            if cur == 0:
                return m
            elif cur == -1:
                r = m-1
            else:
                l = m+1
            m = (l+r)//2
        return m