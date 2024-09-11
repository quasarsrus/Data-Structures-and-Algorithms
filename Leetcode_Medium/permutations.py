# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 20:02:00 2024

@author: apujari1
"""

# Permutations

class Solution:
    
    def permute(self, nums: list[int]) -> list[list[int]]:
        
        output = []
        
        def backtrack(temp):
            
            if len(temp) == len(nums):
                
                output.append(temp[:])
                return
            
            for i in range(len(nums)):
                
                if nums[i] not in temp:
                    
                    temp.append(nums[i])
                    backtrack(temp)
                    temp.pop()
        
        backtrack([])

        return output

if __name__ == "__main__":
    
    nums = [1,2,3]
    
    s = Solution()
    
    print(s.permute(nums))