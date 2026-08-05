class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        #num 5,10,20 bills
        curChange = [0,0,0]

        for bill in bills:
            if bill == 5:
                curChange[0] += 1
            elif bill == 10:
                curChange[0] -= 1
                if curChange[0]<0:
                    return False
                curChange[1] += 1
            elif bill == 20:
                if curChange[1] > 0 and curChange[0] > 0:
                    curChange[1] -= 1
                    curChange[0] -= 1
                elif curChange[0] > 2:
                    curChange[0] -= 3
                else:
                    return False
                curChange[2] += 1
        
        return True