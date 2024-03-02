class Solution:
    def wateringPlants(self, plants: list[int], capacity: int) -> int:
        result = 1 
        temp = capacity

        for i in range(len(plants) - 1):
            temp -= plants[i]  
            if temp < plants[i + 1]:  
                result += (i + 1) * 2 + 1 
                temp = capacity 
            else:
                result += 1  
        return result