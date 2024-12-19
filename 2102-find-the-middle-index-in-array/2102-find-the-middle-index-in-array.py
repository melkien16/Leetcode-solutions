class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        if len(nums) <= 0:
            return
        for i in range(len(nums)):
            leftSum = 0
            rightSum = 0
            leftPtr = 0
            rightPtr = len(nums) - 1
            while leftPtr < i:
                leftSum += nums[leftPtr]
                leftPtr += 1
            while rightPtr > i:
                rightSum += nums[rightPtr]
                rightPtr -= 1
            if rightSum == leftSum:
                return i
        return -1
        