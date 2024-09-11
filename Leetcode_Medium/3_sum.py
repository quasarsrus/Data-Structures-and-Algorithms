# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 20:00:25 2024

@author: apujari1
"""

# 3 Sum
"""
class Solution:
  def threeSum(self, name: list[int]) -> list[list[int]]:

    name = sorted(name)
    result = set()

    i = 0
    while i != len(name):
      j = 0
      k = len(name)-1
      while j < k:
        j += 0 if j != i else 1
        k -= 0 if k != i else 1
        sum = name[j] + name[k]
        if sum == -name[i]:
            a,b,c = sorted([name[i], name[j], name[k]])
            result.add((a,b,c))
            k -= 1
            j += 1
        elif sum > -name[i]:
            k -= 1
        elif sum < -name[i]:
            j += 1
        j += 0 if j != i else 1
        k -= 0 if k != i else 1

      i += 1

    result2 = [i for i in result]

    return result2

"""

# 3 Sum

class Solution:
  def threeSum(self, name: list[int]) -> list[list[int]]:

    name = sorted(name)
    i = 0
    result = []

    while i != len(name):

      if i > 0 and name[i] == name[i-1]:
        i += 1
        continue

      else:
        j = i + 1
        k = len(name) - 1

        while j < k:
            sum = name[j] + name[k]

            if sum == -name[i]:
              result.append([name[i],name[j],name[k]])
              j += 1
              while name[j] == name[j-1] and j < k:
                j += 1
            elif sum > -name[i]:
              k -= 1
            elif sum < -name[i]:
              j += 1
        i += 1

    return result


if __name__ == "__main__":

  nums = [0,0,0]

  s = Solution()

  print(s.threeSum(nums))