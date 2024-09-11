# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 20:09:19 2024

@author: apujari1
"""

#Search in Rotated Sorted Array

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        if len(nums)==1:
          return 0 if nums[0] == target else -1

        while left <= right:
          marker = (left+right)//2

          if nums[marker] == target:
            return marker

          if nums[marker] >= nums[left]:

            if nums[left] <= target and nums[marker] > target:
              right = marker-1
            elif nums[left] <= target and nums[marker] < target:
              left = marker+1
            else:
              left = marker+1

          else:
            if nums[right] >= target and nums[marker] < target:
              left = marker+1
            elif nums[right] >= target and nums[marker] > target:
              right = marker-1
            else:
              right = marker-1

        return -1