# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 20:02:15 2024

@author: apujari1
"""

# Subsets

class Solution:
    
    def subsets(self, nums):
        
        output = []
        nums = sorted(nums)
        def backtrack(index, temp):       
            output.append(temp[:])     
            for i in range(index, len(nums)):
                backtrack(i+1, temp + [nums[i]])
                    
        backtrack(0, [])
                        
        return output
        
if __name__ == "__main__":
    
    nums = [1,2,3]
    
    s = Solution()
    
    print(s.subsets(nums))  