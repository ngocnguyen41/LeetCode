class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = set(nums)
        result = (3*sum(temp) - sum(nums)) // 2
        return result