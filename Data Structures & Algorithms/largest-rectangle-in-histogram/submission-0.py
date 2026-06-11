class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #go right and find next shorted ix to the right
        n = len(heights)
        rShort = [n-1]*(n+2)
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]]>heights[i]:
                rShort[stack.pop()+1] = i-1
            stack.append(i)
        lShort = [0]*(n+2)
        stack = []
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]]>heights[i]:
                lShort[stack.pop()+1] = i+1
            stack.append(i)


        ans = 0

        for i in range(n):
            ans = max(ans, (rShort[i+1]-lShort[i+1])*heights[i]+heights[i])

        return ans
