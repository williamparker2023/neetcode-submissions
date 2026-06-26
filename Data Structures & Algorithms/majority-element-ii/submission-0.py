class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        
        ans = []
        n = len(nums)
        majReq = n//3

        for num in freq:
            if freq[num] > majReq:
                ans.append(num)
        return ans