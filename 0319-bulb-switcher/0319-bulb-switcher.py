class Solution:
    def bulbSwitch(self, n: int) -> int:
        if n == 0:
            return 0
        else:
            count = 1
            for i in range (1, int(sqrt(n))):
                count += 1
        return count