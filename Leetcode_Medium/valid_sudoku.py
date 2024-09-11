# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 19:59:01 2024

@author: apujari1
"""

#Valid Sudoku

class Solution:
  def isvalidsudoku(self, board: list[list[str]]) -> bool:

    for i in range(len(board)):
      row = {}
      for j in range(len(board[i])):
        if ord(board[i][j]) != ord(".") and board[i][j] in row.keys():
          return False
        elif ord(board[i][j]) != ord("."):
          row[board[i][j]] = 1
        else:
          continue

    for i in range(len(board)):
      column = {}
      for j in range(len(board[i])):
        if ord(board[j][i]) != ord(".") and board[j][i] in column.keys():
          return False
        elif ord(board[j][i]) != ord("."):
          column[board[j][i]] = 1
        else:
          continue

    k = 1
    block = {}
    for i in range(len(board)):
      block[i+1] = [0]

    for i in range(len(board)):
      for j in range(len(board[i])):
        if ord(board[j][i]) != ord(".") and board[j][i] in block[k]:
          return False
        elif ord(board[j][i]) != ord("."):
          block[k].append(board[j][i])

        if (j+1)%3 == 0:
          k += 1

      if (i+1)%3 != 0:
        k = k - 3


    return True


if __name__ == "__main__":
  board = [["5","3",".",".","7",".",".",".","."]
  ,["6",".",".","1","9","5",".",".","."]
  ,[".","9","8",".",".",".",".","6","."]
  ,["8",".",".",".","6",".",".",".","3"]
  ,["4",".",".","8",".","3",".",".","1"]
  ,["7",".",".",".","2",".",".",".","6"]
  ,[".","6",".",".",".",".","2","8","."]
  ,[".",".",".","4","1","9",".",".","5"]
  ,[".",".",".",".","8",".",".","7","9"]]

  s = Solution()

  print(s.isvalidsudoku(board))