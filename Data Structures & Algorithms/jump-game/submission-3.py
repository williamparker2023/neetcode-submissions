class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        n = len(nums)

        while i<n-1:
            numJumps = nums[i]
            if numJumps == 0:
                return False
            nextIx = i
            nextVal = 0
            for j in range(i+1,min(i+numJumps+1,n)):
                tempJumps = nums[j] + j - i
                if tempJumps >= nextVal:
                    nextIx = j
                    nextVal = tempJumps
            if nextIx == i:
                return False
            i = nextIx


        return True 