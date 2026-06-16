class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        startIx = -1
        startVal = sys.maxsize
        cur = 0
        n = len(gas)

        for i in range(n):
            cur += gas[i]-cost[i]
            if cur < startVal:
                startVal = cur
                startIx = (i+1)%n
        curGas = 0
        for i in range(startIx,n):
            curGas += gas[i]-cost[i]
            if curGas < 0:
                return -1
        for i in range(0,startIx):
            curGas += gas[i]-cost[i]
            if curGas < 0:
                return -1
        return startIx