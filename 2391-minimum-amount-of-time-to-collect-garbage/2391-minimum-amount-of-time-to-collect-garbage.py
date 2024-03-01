class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        time = 0
        timeM = 0
        timeP = 0
        timeG = 0 
        for i in range(len(garbage) - 1, -1, -1):
            time += len(garbage[i]) 

            if "G" in garbage[i] and timeG == 0:
                timeG += sum(travel[:i])

            if "M" in garbage[i] and timeM == 0:
                timeM += sum(travel[:i])

            if "P" in garbage[i] and timeP == 0:
                timeP += sum(travel[:i])
            
        result = time + timeG + timeM + timeP
        return result