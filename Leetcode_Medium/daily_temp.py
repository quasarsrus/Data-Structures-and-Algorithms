# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 20:13:41 2024

@author: apujari1
"""

#Daily Temperatures

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result = [0]*len(temperatures)
        stack = []

        for i in range(len(temperatures)-1):
            if temperatures[i+1] > temperatures[i]:
                result[i] = 1
                done = False
                j = len(stack)-1
                while (not done) and stack:
                    if stack[j][0] < temperatures[i+1]:
                        result[stack[j][1]] = i+1 - stack[j][1]
                        stack.pop()
                        j -= 1
                    else:
                        done = True
            else:
                stack.append([temperatures[i],i])

        return result