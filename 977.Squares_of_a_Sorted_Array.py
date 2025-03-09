class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        low, high = 0, n-1
        index = n - 1

        while low <= high:
            if abs(nums[low]) > abs(nums[high]):
                result[index] = nums[low]**2
                low += 1
            else:
                result[index] = nums[high]**2
                high -= 1
            index -= 1

        return result
