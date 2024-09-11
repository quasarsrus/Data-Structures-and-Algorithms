# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 19:57:55 2024

@author: apujari1
"""

# Product of Array Except Self

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        left = [0] * len(nums)
        right = [0] * len(nums)
        
        j = len(nums)-1
        for i in range(len(nums)):
            if i == 0:
                left[i] = 1 * nums[i]
                right[j] = 1 * nums[j]
                j -= 1
                
            else:   
                left[i] = left[i-1] * nums[i]   
                right[j] = right[j+1] * nums[j]
                j -= 1
                
        return_list = [0] * len(nums)
        
        print(left)
        print(right)
                
        for i in range(len(nums)):
            
                if i == 0:
                    return_list[i] = 1 * right[i+1]
                    
                elif i == len(nums)-1:
                    return_list[i] = left[i-1] * 1
                    
                else:
                    return_list[i] = left[i-1] * right[i+1]
        
        return return_list


if __name__ == "__main__":
    
    input_list = [-1,1,0,-3,3]
    s = Solution()
    print(s.productExceptSelf(input_list))