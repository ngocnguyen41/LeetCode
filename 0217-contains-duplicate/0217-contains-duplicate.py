class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        temp = {}
        for i in nums:
            if i in temp:
                return True
            temp[i] = 1
        return False