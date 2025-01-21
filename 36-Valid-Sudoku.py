class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Brute force:

        # #Making hashsets for each row, if one number is seen more than once, return False:
        # for row in range(9):
        #     seen = set()
        #     for i in range(9):
        #         if board[row][i] == \.\:
        #             continue
        #         if board[row][i] in seen:
        #             return False
        #         seen.add(board[row][i])
        # #Making hashsets for each col, if one number is seen more than once, return False:
        # for col in range(9):
        #     seen = set()
        #     for i in range(9):
        #         if board[i][col] == \.\:
        #             continue
        #         if board[i][col] in seen:
        #             return False
        #         seen.add(board[i][col])
        # #Making hashsets for each square:
        # for square in range(9):
        #     seen = set()
        #     for i in range(3):
        #         for j in range(3):
        #             #square // 3 gives the row, and the * 3 + i does the encoding:
        #             row = (square // 3) * 3 + i
        #             #square % 3 gives the col, and the * 3 + j does the encoding:
        #             col = (square % 3) * 3 + j
        #             if board[row][col] == \.\:
        #                 continue
        #             if board[row][col] in seen:
        #                 return False
        #             seen.add(board[row][col])
        # return True

        #Using bitmask:Reducing the space complexity:

        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9
        for r in range(9):
            for c in range(9):
                if board[r][c] == \.\:
                    continue
                #1 << val creates a bitmask with only the val-th bit set:
                #& checks if the val-th bit is already set in the corresponding row/col/square:
                val = int(board[r][c]) - 1 #because we will change the bit of the index (0 to 8)
                if (1 << val) & rows[r]:
                    return False
                if (1 << val) & cols[c]:
                    return False
                if (1 << val) & squares[(r//3) * 3 + (c//3)]:
                    return False
                
                #|= sets the val-th bit in the corresponding row/column/square bitmask to indicate that this digit has been seen:
                rows[r] |= (1 << val)
                cols[c] |= (1 << val)
                squares[(r // 3) * 3 + (c // 3)] |= (1 << val)
        return True