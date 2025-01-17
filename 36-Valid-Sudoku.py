class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Brute force:

        #Making hashsets for each row, if one number is seen more than once, return False:
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == \.\:
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])
        #Making hashsets for each col, if one number is seen more than once, return False:
        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == \.\:
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])
        #Making hashsets for each square:
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    #square // 3 gives the row, and the * 3 + i does the encoding:
                    row = (square // 3) * 3 + i
                    #square % 3 gives the col, and the * 3 + j does the encoding:
                    col = (square % 3) * 3 + j
                    if board[row][col] == \.\:
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True
