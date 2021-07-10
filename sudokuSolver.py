import time

class Sudoku():
  sudokuProblem = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

def printBoard(board):
  print("- - - - - - - - - - - - -")
  for row in range(len(board)):
    print('| ', end='')
    for col in range(len(board[row])):
      print(board[row][col], end = ' ')
      if col % 3 == 2:
        print('| ', end='')
    print('')
    if row % 3 == 2:
      print("- - - - - - - - - - - - -")

def inRow(board, guessRow, guessNum):
  for col in board[guessRow]:
    if col == guessNum:
      return True
  return False

def inCol(board, guessCol, guessNum):
  for row in range(len(board)):
    if board[row][guessCol] == guessNum:
      return True
  return False

def inBlock(board, row, col, guessNum):
  startRow = row - row % 3
  startCol = col - col % 3
  for i in range(startRow, startRow + 3):
    for j in range(startCol, startCol + 3):
      if board[i][j] == guessNum:
        return True
  return False

def isValid(board, row, col, guessNum):
  if (inRow(board, row, guessNum)): return False
  if (inCol(board, col, guessNum)): return False
  if (inBlock(board, row, col, guessNum)): return False
  return True

def getNextBlank(board, row, col):
  while (row < 9):
    while (col < 9):
      if board[row][col] == 0:
        return row, col
      col += 1
    col = 0
    row += 1
  return None

def solveSudoku(board, row = 0, col = 0):
  NextBlank = getNextBlank(board, row, col)
  if (NextBlank == None):
    print("finish")
    return True
  row, col = NextBlank

  for guessNum in range(1, 10):
    if (not isValid(board, row, col, guessNum)):
      continue
    board[row][col] = guessNum
    if solveSudoku(board, row, col):
      return True
    board[row][col] = 0
  return False

def main():
  startTime = time.time()
  board = Sudoku.sudokuProblem
  printBoard(board)
  solveSudoku(board)
  printBoard(board)
  print("runtime: ", time.time()-startTime, "s")

main()
