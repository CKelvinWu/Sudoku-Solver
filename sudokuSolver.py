import time

class Solution:
    def __init__(self, board):
        self.board = board

    def solveSudoku(self, row = 0, col = 0):
        NextBlank = self.getNextBlank(row, col)
        if (NextBlank == None):
            return True
        row, col = NextBlank
        for guessNum in range(1, 10):
            if (not self.isValid(row, col, str(guessNum))):
                continue
            self.board[row][col] = str(guessNum)
#            -----print solve process-----------
#            self.printBoard()
#            time.sleep(0.1)
            if self.solveSudoku(row, col):
                return True
            self.board[row][col] = "."
        return False

    def solveSudokuReverse(self, row = 0, col = 0):
        NextBlank = self.getNextBlank(row, col)
        if (NextBlank == None):
            return True
        row, col = NextBlank
        for guessNum in range(9, 0, -1):
            if (not self.isValid(row, col, str(guessNum))):
                continue
            self.board[row][col] = str(guessNum)
#            -----print solve process-----------
#            self.printBoard()
#            time.sleep(0.1)
            if self.solveSudokuReverse(row, col):
                return True
            self.board[row][col] = "."
        return False

    def inRow(self, guessRow, guessNum):
        for col in self.board[guessRow]:
            if col == guessNum:
                return True
        return False

    def inCol(self, guessCol, guessNum):
        for row in range(len(self.board)):
            if self.board[row][guessCol] == guessNum:
                return True
        return False

    def inBlock(self, row, col, guessNum):
        startRow = row - row % 3
        startCol = col - col % 3
        for i in range(startRow, startRow + 3):
            for j in range(startCol, startCol + 3):
                if self.board[i][j] == guessNum:
                    return True
        return False

    def isValid(self, row, col, guessNum):
        if (self.inRow(row, guessNum)): return False
        if (self.inCol(col, guessNum)): return False
        if (self.inBlock(row, col, guessNum)): return False
        return True

    def getNextBlank(self, row, col):
        while (row < 9):
            while (col < 9):
                if self.board[row][col] == ".":
                    return row, col
                col += 1
            col = 0
            row += 1
        return None

    def printBoard(self):
        print("- - - - - - - - - - - - -")
        for row in range(len(self.board)):
            print('| ', end='')
            for col in range(len(self.board[row])):
                print(self.board[row][col], end = ' ')
                if col % 3 == 2:
                    print('| ', end='')
            print('')
            if row % 3 == 2:
                print("- - - - - - - - - - - - -")
def main():
    startTime = time.time()
    board = [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
            ]
    boardRev = [x[:] for x in board]
    sol = Solution(board)
    sol.printBoard()
    sol.solveSudoku()
    sol.printBoard()
    solRev = Solution(boardRev)
    solRev.solveSudokuReverse()
    solRev.printBoard()
    if sol.board == solRev.board:
        print("This problem has unique solution")
    else:
        print("This problem has multiple solution")
    print("runtime: ", time.time()-startTime, "s")
main()