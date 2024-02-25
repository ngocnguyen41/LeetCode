class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        result = 0
        
        for i in range (len(satisfaction)):
            sumSatisfaction, k = 0, 1
            for j in range(i, len(satisfaction)):
                sumSatisfaction += satisfaction[j] * k
                k += 1

            if(satisfaction[0] >= 0):
                return sumSatisfaction

            result = max(result, sumSatisfaction)
        return result
