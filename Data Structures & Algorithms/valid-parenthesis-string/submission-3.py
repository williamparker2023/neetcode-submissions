class Solution:
    def checkValidString(self, s: str) -> bool:
        leftStack = []
        starStack = []
        n = len(s)

        for i in range(n):
            if s[i] == "(":
                leftStack.append(i)
            elif s[i] == "*":
                starStack.append(i)
            else:
                if len(leftStack)>0:
                    leftStack.pop()
                elif len(starStack)>0:
                    starStack.pop()
                else:
                    return False
        
        if len(leftStack)>len(starStack):
            return False
        
        while leftStack:
            if leftStack[-1]<starStack[-1]:
                leftStack.pop()
                starStack.pop()
            else:
                return False
        return True