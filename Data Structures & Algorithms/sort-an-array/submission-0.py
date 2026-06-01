class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr1,arr2):
            if len(arr1) == 0:
                return arr2
            half1 = len(arr1)//2
            newArr1 = merge(arr1[:half1],arr1[half1:])
            half2 = len(arr2)//2
            newArr2 = merge(arr2[:half2],arr2[half2:])
            sortedArr = []
            p1,p2 = 0,0
            while p1<len(newArr1) and p2<len(newArr2):
                if newArr1[p1] <= newArr2[p2]:
                    sortedArr.append(newArr1[p1])
                    p1+=1
                else:
                    sortedArr.append(newArr2[p2])
                    p2+=1
            if p1<len(newArr1):
                sortedArr = sortedArr + newArr1[p1:]
            elif p2<len(newArr2):
                sortedArr = sortedArr + newArr2[p2:]
            return sortedArr
        half = len(nums)//2
        return merge(nums[:half],nums[half:])