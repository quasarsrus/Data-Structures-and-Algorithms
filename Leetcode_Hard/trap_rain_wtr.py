# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 20:14:54 2024

@author: apujari1
"""

class Solution:
    def trap(self, height: list[int]) -> int:
        stack_right = []
        stack_left = []
        area_left = 0
        area_right = 0
        
        for i in range(len(height)-1, -1,-1):
            if i == len(height)-1:
                stack_right.append([height[i],i])
                continue
            if stack_right[-1][0] <= height[i]:
                area_right = area_right + (min(stack_right[-1][0], height[i])\
                                           * (stack_right[-1][1] - i - 1) \
                                               - (sum(height[(i+1):stack_right[-1][1]])))
                stack_right.pop()
                stack_right.append([height[i],i])
        
        
        for i in range(stack_right[-1][1]+1):
            if i == 0:
                stack_left.append([height[i],i])
                continue
            
            if stack_left[-1][0] <= height[i]:
                area_left = area_left + (min(stack_left[-1][0], height[i]) \
                                         * (i - stack_left[-1][1] - 1) \
                                             - sum(height[(stack_left[-1][1]+1):i]))
                stack_left.pop()
                stack_left.append([height[i],i])
        
        return (area_left+area_right)