# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 19:58:20 2024

@author: apujari1
"""

# Min Stack

class MinStack:
    
    def __init__(self):
        self.stack = []
        self.min_list = []
    
    def push(self, val: int) -> None:
        
        if self.stack:
            if val <= self.min_list[-1]:
                self.min_list.append(val)
        else:
            self.min_list.append(val)
        
        self.stack.append(val)
        
        return 
    
    def pop(self) -> None:
        
        temp = self.stack.pop()
        
        if temp != self.min_list[-1]:
            return
        else:
            self.min_list.pop()        
        return
    
    def top(self) -> int:
        
        return self.stack[-1]
    
    def getMin(self) -> int:
        
        return self.min_list[-1]
    
        

if __name__=="__main__":
    
    s = MinStack()