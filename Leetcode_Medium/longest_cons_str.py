# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 19:59:17 2024

@author: apujari1
"""

#Longest Consecutive String

class Solution:
  def longestConsecutive(self, nums: list[int]) -> int:

    temp = set(nums)

    result = []

    for i in temp:
      k = 1
      if i-1 not in temp:
        j = 1
        while i+j in temp:
          k += 1
          j += 1
        result.append(k)
      else:
        continue

    if result:
      return max(result)
    else:
      return 0
  

if __name__ == "__main__":
  nums = []

  s = Solution()

  print(s.longestConsecutive(nums))