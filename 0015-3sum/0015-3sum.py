class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()

        for i in range (len(nums) - 2):           
            left = i + 1
            right = len(nums) - 1

            while left < right:
                sumNums = nums[i] + nums[left] + nums[right]

                if sumNums == 0 :
                    result.add((nums[i], nums[left], nums[right]))
                    right -= 1

                elif sumNums > 0:
                    right -= 1

                else:
                    left += 1

        return result