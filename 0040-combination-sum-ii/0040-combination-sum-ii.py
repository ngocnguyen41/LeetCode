class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def backtrack (arr, sumArr, index):
            if sumArr > target:
                return 
            if sumArr == target:
                result.append(arr[:])
                return 

            
            for i in range (index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                    
                arr.append(candidates[i])
                sumArr += candidates[i]

                backtrack(arr, sumArr, i + 1)

                arr.pop()
                sumArr -= candidates[i]

        backtrack([], 0, 0)


        return result