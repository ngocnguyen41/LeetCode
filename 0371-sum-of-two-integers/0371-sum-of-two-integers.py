class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b != 0:
            temp = (a & b) << 1
            a = (a ^ b) & mask
            b = temp & mask

        if a <= 0x7FFFFFFF:
            return a
        else:
            return ~(a ^ mask)  