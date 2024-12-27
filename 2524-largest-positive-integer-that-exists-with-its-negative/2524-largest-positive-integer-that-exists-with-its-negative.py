class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        largest = -1
        for i in nums:
            if i > 0 and -i in nums and i > largest:
                largest = i
        return largest