class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        temp = nums1 + nums2 
        temp.sort()

        n = len(temp)

        if len(temp) % 2 == 1:
            return temp[n // 2]

        else:
            return (temp[n // 2] + temp[n // 2 - 1]) / 2
