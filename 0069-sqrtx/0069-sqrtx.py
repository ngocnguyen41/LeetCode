class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        elif x == 1:
            return 1

        first = 0
        last = x
         
        while first <= last:
            mid = (last + first) // 2

            if (mid == x / mid):
                return mid
            elif mid > x / mid:
                last = mid - 1
            else:
                first = mid + 1
        return last