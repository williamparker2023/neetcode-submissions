class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 0
            dic[num] = dic[num] + 1
        bigCount = 0
        bigNum = 0
        for num in dic:
            if dic[num]>bigCount:
                bigNum = num
                bigCount = dic[num]
        return bigNum