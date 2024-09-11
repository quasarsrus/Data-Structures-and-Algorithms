# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 20:00:11 2024

@author: apujari1
"""

# Two sum II

class Solution:
  def twoSum(self, numbers: list[int], target:int) -> list[int]:

    sample = dict()

    for i,j in enumerate(numbers):
      if target - j not in sample.keys():
        sample[j] = i+1
      else:
        if target - j != j:
          sample[j] = i+1
          return [sample[target-j], sample[j]]

        else:
          return [sample[target-j],i+1]
"""   
# Two Sum II

class Solution:
  def twoSum(self, numbers: list[int], target:int) -> list[int]:

    i = 0
    j = len(numbers)-1

    while i<=j:
      sum = numbers[i] + numbers[j]
      if sum == target:
        return [i+1,j+1]
      elif sum > target:
        j -= 1
      elif sum < target:
        i += 1
        
if __name__=="__main__":
  numbers = [0,0,3,4]
  target = 0

  s = Solution()

  print(s.twoSum(numbers,target))