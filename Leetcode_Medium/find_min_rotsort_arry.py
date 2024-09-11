# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 20:08:08 2024

@author: apujari1
"""

#Find Minimum in Rotated Sorted Array

class Solution:
    def findMin(self, nums: list[int]) -> int:
        left = 0
        right = len(nums)-1

        if len(nums)==1:
          return nums[0]

        while left <= right:
          marker = (left+right)//2

          if nums[marker] >= nums[left]:
            val = nums[left]
            left = marker+1
          else:
            val = nums[marker]
            right = marker-1

          if nums[left] <= nums[right]:
            return min(nums[left], val)