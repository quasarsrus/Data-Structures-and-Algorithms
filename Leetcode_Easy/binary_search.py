# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 20:07:25 2024

@author: apujari1
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = int(len(nums)/2)

        def binarysearch(val, arr, tok):

          if not arr:
              return -1
          elif len(arr) == 1 and arr[0] != target:
            return -1

          if target > arr[val]:

              tok = tok + int(len(arr[val+1:])/2) + 1
              sol = binarysearch(int(len(arr[val+1:])/2),arr[val+1:], tok)

          elif target < arr[val]:
              if val%2 == 0:
                tok = tok - int(len(arr[:val])/2)
              else:
                tok = tok - int(len(arr[:val])/2) - 1
              sol = binarysearch(int(len(arr[:val])/2),arr[:val], tok)        
          else:
            return tok

          return sol

        return binarysearch(n, nums, n)