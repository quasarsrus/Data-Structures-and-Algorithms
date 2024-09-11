# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 20:01:07 2024

@author: apujari1
"""

# Container with Most Water

class Solution:
  def maxArea(self, height: list[int]) ->int:

    i = 0
    j = len(height) - 1
    maxarea = 0

    while i < j:
      maxarea = max(maxarea, min(height[i], height[j])*(j-i))

      if height[j] < height[i]:
        j -= 1
      else:
        i += 1

    return maxarea

if __name__ == "__main__":
  height = [1,8,6,2,5,4,8,3,7]
  s = Solution()

  print(s.maxArea(height))