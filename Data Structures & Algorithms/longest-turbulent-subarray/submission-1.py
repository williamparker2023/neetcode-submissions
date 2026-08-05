class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        #[bigs are evens, bigs are odds]
        maxTurb = [[1,1] for _ in range(n)]

        for i in range(1,n):
            if i % 2 == 0:
                if arr[i] > arr[i-1]:
                    maxTurb[i][0] = maxTurb[i-1][0] + 1
                elif arr[i] < arr[i-1]:
                    maxTurb[i][1] = maxTurb[i-1][1] + 1
            else:
                if arr[i] > arr[i-1]:
                    maxTurb[i][1] = maxTurb[i-1][1] + 1
                elif arr[i] < arr[i-1]:
                    maxTurb[i][0] = maxTurb[i-1][0] + 1
        
        big = 0
        for i in range(n):
            big = max(big,max(maxTurb[i]))
        return big