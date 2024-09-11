# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 19:54:43 2024

@author: apujari1
"""
# Valid Parenthesis

class Solution:
    def isValid(self, s:str) -> bool:
            
        
        stack = []
        ref = {'(':2, ')':2, '{':3, '}':3, '[':4, ']':4}
    
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            else:
                if stack:
                    
                    temp = stack.pop()
                    if ref[temp] % ref[i] == 0:
                        continue
                    else:
                        return False
                else:
                    return False
                
        if stack:
            return False
        else:
            return True
    

if __name__=="__main__":
    
    string = ")"
    
    s = Solution()
    
    print(s.isValid(string))