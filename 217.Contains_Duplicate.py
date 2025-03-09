class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        result = {}
        for i in nums:
            if i in result:
                result[i] += 1
                return True
            else:
                result[i] = 1
        return False
