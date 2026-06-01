class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        m = (l+r)//2
        
        smallHours = r

        def hoursNeeded(rate):
            temp = 0
            for pile in piles:
                temp += pile//rate
                if pile%rate != 0:
                    temp+=1
            return temp
        
        while l<=r:
            curHours = hoursNeeded(m)
            if curHours>h:
                l = m+1
            else:
                r = m-1
                smallHours = min(m,smallHours)
            m = (l+r)//2
        

        return smallHours