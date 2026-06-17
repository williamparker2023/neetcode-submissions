class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        n = len(numbers)
        for i in range(n):
            needed = target-numbers[i]
            if needed in seen:
                return [seen[needed]+1,i+1]
            seen[numbers[i]] = i
        return []