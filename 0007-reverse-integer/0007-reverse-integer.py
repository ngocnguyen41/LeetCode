class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        while x != 0:
            if x > 0:
                temp = x % 10
            else:
                temp = x % -10

            result = result * 10 + temp
            x = trunc(x / 10)
        
        if (result <= pow(-2, 31) or result > pow(2, 31)):
            return 0
        
        return result
