class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        valid = set()
        seen = set()
        seen.add(nums[0])
        n = len(nums)

        for i in range(1,n-1):
            for j in range(i+1,n):
                needed = -(nums[i]+nums[j])
                if needed in seen:
                    valid.add(tuple(sorted((needed,nums[i],nums[j]))))
            seen.add(nums[i])
        ans = []
        for tup in valid:
            ans.append(list(tup))
        return ans