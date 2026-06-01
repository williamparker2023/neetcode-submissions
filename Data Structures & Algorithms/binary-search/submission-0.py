class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        m = (l+r)//2

        while l<=r:
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m+1
            else:
                r = m-1
            m = (l+r)//2
        return -1