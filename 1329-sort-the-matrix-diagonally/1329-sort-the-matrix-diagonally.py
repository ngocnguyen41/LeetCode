class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        temp = {}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i - j not in temp:
                    temp[i - j] = []
                temp[i - j].append(mat[i][j])

        for i in temp.values():
            i.sort()

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] = temp[i - j].pop(0)

        return mat
