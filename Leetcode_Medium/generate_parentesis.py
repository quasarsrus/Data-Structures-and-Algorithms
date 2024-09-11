# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 20:01:44 2024

@author: apujari1
"""

# Generate Parentheses

class Solution:
    
    def gnp(self, n: int) -> list[str]:
        
        output = []
        
        def backtrack(left, right, string):
            
            if len(string) == n*2:
                output.append(string)
                return
            if left < n:
                backtrack(left+1, right, string + '(')
            if right < left:
                backtrack(left, right+1, string + ')')
            
        
        backtrack(0,0,'')     
        return output




if __name__ == "__main__":
    
    n = 2;
    s = Solution();
    print(s.gnp(n))