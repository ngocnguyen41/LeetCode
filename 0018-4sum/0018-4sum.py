class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = set()

        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                left = j + 1
                right = len(nums) - 1

                while left < right:
                    sumNums = nums[i] + nums[j] + nums[left] + nums[right]

                    if sumNums == target:
                        result.add((nums[i], nums[j], nums[left], nums[right]))
                        right -= 1
                    
                    elif sumNums > target:
                        right -= 1

                    else:
                        left += 1

        return result
                    
