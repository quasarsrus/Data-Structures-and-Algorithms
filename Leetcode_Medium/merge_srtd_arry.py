# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 20:00:36 2024

@author: apujari1
"""

# Merge Sorted Array

nums1 = [0,0,3,0,0,0,0,0,0]
nums2 = [-1,1,1,1,2,3]

m = 3
n = 6

last = m + n - 1

while m > 0 and n > 0:


  if nums1[m - 1] > nums2[n - 1]:
    nums1[last] = nums1[m - 1]
    m -= 1
  else:
    nums1[last] = nums2[n - 1]
    n -= 1
  last -= 1

while n > 0:
  nums1[last] = nums2[n - 1]
  n, last = n - 1, last - 1