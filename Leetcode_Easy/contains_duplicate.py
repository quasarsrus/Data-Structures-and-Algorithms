# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 19:48:45 2024

@author: apujari1
"""

# Contains Duplicate

class Solution:
    def cd(self, nums) -> bool:
        a = {}
        for i in range(len(nums)):
            if int(nums[i]) not in a.values():
                a[i] = int(nums[i])
            else:
                return True
        print(a)
        return False
    
if __name__=="__main__":
    input_list = []
    while True:
        input_list.append(input())
        if input_list[-1] == '':
            del input_list[-1]
            break
    
    s = Solution()
    print(s.cd(input_list))