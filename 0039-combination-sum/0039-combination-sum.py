class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack (arr, sumArr, index):
            if sumArr > target:
                return 
            if sumArr == target:
                result.append(arr[:])
                return 

            
            for i in range (index, len(candidates)):
                arr.append(candidates[i])
                sumArr += candidates[i]

                backtrack(arr, sumArr, i)

                arr.pop()
                sumArr -= candidates[i]

        backtrack([], 0, 0)
        return result



