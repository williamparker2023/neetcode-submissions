class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        reds = 0
        whites = 0
        blues = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                reds += 1
            elif nums[i] == 1:
                whites += 1
            else:
                blues += 1
        
        for i in range(reds):
            nums[i] = 0
        for i in range(reds,reds+whites):
            nums[i] = 1
        for i in range(reds+whites,n):
            nums[i] = 2
        return