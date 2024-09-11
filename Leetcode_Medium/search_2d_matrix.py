# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 20:07:54 2024

@author: apujari1
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = int(len(matrix)/2)
        column = int(len(matrix[0])/2)

        def binsearch(row, column, mat):

          if not mat:
            return False

          if mat[row][column] > target:

            if target > mat[row][0]:
              bool_val = binsearch(0, int(column/2), [mat[row][:column]])
            elif  target < mat[row][0]:
              bool_val = binsearch(int(row/2), column, mat[:row])
            else:
              return True

          elif mat[row][column] < target:

            if target < mat[row][-1]:
              bool_val = binsearch(0, int(len(mat[row][column+1:])/2), [mat[row][column+1:]])
            elif target > mat[row][-1]:
              bool_val = binsearch(int(len(mat[row+1:])/2), column , mat[row+1:])
            else:
              return True
          else:
            return True

          return bool_val


        return binsearch(row,column,matrix)