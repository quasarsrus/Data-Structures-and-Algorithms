# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 20:06:30 2024

@author: apujari1
"""

# Largest Rectangle Histogram


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        position = []
        height = []
        max_area = 0

        for i in range(len(heights)):

          if not position and not height:
            position.append(i)
            height.append(heights[i])
            continue

          if heights[i] >= height[-1]:
            position.append(i)
            height.append(heights[i])

          else:
              while True:

                temp_height = height.pop()
                temp_area = temp_height * (i - position[-1])

                if temp_area > max_area:
                  max_area = temp_area
                if height:
                  if height[-1] > heights[i]:
                    position.pop()
                  else:
                    height.append(heights[i])
                    break

                else:
                  if temp_height > heights[i]:
                    height.append(heights[i])
                    break
                  else:
                    position.pop()
                    position.append(i)
                    height.append(heights[i])
                    break


        if position:
          t = len(position)
          for i in range(t):
            temp_pos = position.pop()
            temp_height = height.pop()

            temp_area = temp_height * (len(heights) - temp_pos)
            if temp_area > max_area:
                max_area = temp_area

        return max_area