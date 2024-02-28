class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            rows = []
            cols = []
            boxes = []

            for col in range(9):
                if board[row][col] != ".":
                    if board[row][col] in rows:
                        return False
                    rows.append(board[row][col])
                
                if board[col][row] != ".":
                    if board[col][row] in cols:
                        return False
                    cols.append(board[col][row])

                rowIndex = 3 * (row // 3) + col // 3
                colIndex = 3 * (row % 3) + col % 3

                if board[rowIndex][colIndex] != ".":
                    if board[rowIndex][colIndex] in boxes:
                        return False   
                    boxes.append(board[rowIndex][colIndex])
                             
        return True