class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        result = []

        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                left = mid
                right = mid

                while left > 0 and nums[left - 1] == target:
                    left = left - 1

                while right < len(nums) - 1 and nums[right + 1] == target:
                    right = right + 1
                    
                result.append(left)
                result.append(right)
                break

            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        if result != []:
            return result
        else:   
            return [-1, -1]
        
