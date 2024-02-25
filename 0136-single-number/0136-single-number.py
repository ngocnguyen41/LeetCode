class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = 0
        for i in range (len(nums)):
            temp = temp^nums[i]
        return temp

        # temp = set(nums)
        # result = (3*sum(temp) - sum(nums)) // 2
        # return result