class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        oneRow = [0] * m
        oneCol = [0] * n
        zeroRow = [0] * m
        zeroCol = [0] * n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    oneRow[i] += 1
                else:
                    zeroRow[i] += 1
        
        for i in range(n):
            for j in range(m):
                if grid[j][i] == 1:
                    oneCol[i] += 1
                else:
                    zeroCol[i] += 1
        
        print(f' {oneRow}, {oneCol} and {zeroRow}, {zeroCol}')

        diff = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                diff[i][j] = oneRow[i] + oneCol[j] - zeroRow[i] - zeroCol[j]

        return diff