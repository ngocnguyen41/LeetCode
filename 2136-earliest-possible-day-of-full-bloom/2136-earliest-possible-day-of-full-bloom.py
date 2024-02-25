class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        plantAndGrowTime = list(zip(plantTime, growTime))
        plantAndGrowTime.sort(key = lambda x: x[1], reverse=True)

        startTime = 0
        result = 0

        for plant, grow in plantAndGrowTime: 
            result = max(result, startTime + grow + plant)
            startTime += plant
            
        return result