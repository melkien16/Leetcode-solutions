class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        newNums = []
        appendedNum = ''
        sum = 0
        while len(nums) > 0:
            lastPtr = len(nums) - 1
            firstPtr = 0
            if lastPtr == firstPtr:
                newNums.append(nums[firstPtr])
                nums.pop(firstPtr)
            if lastPtr != firstPtr:
                appendedNum = str(nums[firstPtr]) + str(nums[lastPtr])
                newNums.append(int(appendedNum))
                nums.pop(lastPtr)
                nums.pop(firstPtr)
        for i in newNums:
            sum += i
        return sum