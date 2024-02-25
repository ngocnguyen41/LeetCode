class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        temp1 = arr1[0]    
        temp2 = arr2[0]   

        for i in range (1, len(arr1)):
            temp1 ^= arr1[i]

        for i in range (1, len(arr2)):
            temp2 ^= arr2[i]
        
        return temp1 & temp2


 