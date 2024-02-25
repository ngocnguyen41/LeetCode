class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(mat):
            n = len(mat)

            for i in range(n):
                for j in range(i + 1, n):
                    temp = mat[i][j]
                    mat[i][j] = mat[j][i]
                    mat[j][i] = temp

            for i in range(n):
                left = 0
                right = n - 1
                while (left < right):
                    temp = mat[i][left]
                    mat[i][left] = mat[i][right]
                    mat[i][right] = temp
                    left += 1
                    right -= 1
            return mat
            
        for i in range(4):
            if rotate(mat) == target:
                return True
            else:
                continue
        return False        