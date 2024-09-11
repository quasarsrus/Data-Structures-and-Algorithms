# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 20:01:25 2024

@author: apujari1
"""

# Evaluate Reverse Polish Notation

class Solution:
    
    def evalRPN(self, tokens: list[str]) -> int:
        
        stack = []
        operation = {'+': (lambda x,y: x + y), '-': (lambda x,y: x - y), \
                     '*': (lambda x,y: x * y), '/': (lambda x,y: x / y)}
        
        for i in tokens:
            
            if i not in operation.keys():
                stack.append(int(i))
                
            else:
                temp1 = stack.pop()
                temp2 = stack.pop()      
                stack.append(int(operation[i](temp2,temp1)))
        
        return stack.pop()
    
if __name__ == "__main__":
    
    tokens = ["2","1","+","3","*"]
    
    s = Solution()
    
    print(s.evalRPN(tokens))