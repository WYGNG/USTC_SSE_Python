import random

def main():
    n = eval(input("Enter the length of a square matrix: "))
    
    board = []
    isSameOnARow = False
    isSameOnAColumn = False
    isSameOnADiagonal = False
    isSameOnASubdiagonal = False

    for i in range(n):
        board.append([])
        for j in range(n):
            board[i].append(random.randint(0, 1)) 
            print(board[i][j], end = "")
        print()

    # Check rows
    for i in range(n):
      same = True
      for j in range(1, n):
        if board[i][0] != board[i][j]:
          same = False
          break

      if same:
        print("All " + board[i][0] + "'s on row " + i)
        isSameOnARow = True

    # Check columns
    for j in range(n):
      same = True
      for i in range(1, n):
        if board[0][j] != board[i][j]:
          same = False
          break

      if same:
        print("All " + str(board[0][j]) + "'s on column " + str(j))
        isSameOnAColumn = True

    # Check major diagonal
    same = True
    for i in range(1, n):
      if board[0][0] != board[i][i]:
        same = False
        break

    if same:
      print("All " + str(board[0][0]) + "'s on major diagonal")
      isSameOnADiagonal = True

    # Check subdiagonal
    same = True
    for i in range(1, n):
      if board[0][n - 1] != board[i][n - 1 - i]:
        same = False
        break

    if same:
      print("All " + str(board[0][n - 1]) + "'s on sub-diagonal")
      isSameOnASubdiagonal = True
    
    if not isSameOnARow: 
      print("No same numbers on a row")

    if not isSameOnAColumn:
      print("No same numbers on a column")

    if not isSameOnADiagonal: 
      print("No same numbers on the major diagonal")

    if not isSameOnASubdiagonal: 
      print("No same numbers on the sub-diagonal")

main()
