class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        trapped = [0]*n
        leftTall = [0]*n
        rightTall = [0]*n

        for i in range(1,n):
            leftTall[i] = max(leftTall[i-1],height[i-1])
        for i in range(n-2,-1,-1):
            rightTall[i] = max(rightTall[i+1],height[i+1])
        
        for i in range(n):
            water = min(leftTall[i],rightTall[i]) - height[i]
            trapped[i] = max(water,0)
        
        return sum(trapped)