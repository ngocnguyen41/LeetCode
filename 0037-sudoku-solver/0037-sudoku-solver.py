class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """


        def isValid(board, row, col, c):
            for i in range (9):
                if board[i][col] == c:
                    return False
                if board[row][i] == c:
                    return False

                rowIndex = 3 * (row // 3) + (i // 3)
                colIndex = 3 * (col // 3) + (i % 3)

                if board[rowIndex][colIndex] == c:
                    return False
            return True

        chars = "123456789"

        def solve(board):
            for row in range (len(board)):
                for col in range(len(board[0])):
                    if board[row][col] == ".":
                        for c in chars:
                            if isValid(board, row, col, c):
                                board[row][col] = c
                                if solve(board):
                                    return True
                                else:
                                    board[row][col] = "."
                        return False
            return True
        solve(board) 