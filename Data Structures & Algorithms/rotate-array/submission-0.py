class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        visited = set()

        for i in range(n):
            ix = i
            prev = nums[i]

            ix = (ix + k) % n
            while ix not in visited:
                nex = nums[ix]
                nums[ix] = prev
                prev = nex
                visited.add(ix)
                ix = (ix + k) % n