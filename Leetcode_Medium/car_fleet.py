# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 20:02:45 2024

@author: apujari1
"""

# Car Fleet

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        
        combined = []
        for i in range(len(position)):
            combined.append((position[i], speed[i]))
            
        combined.sort()
        
        stack = []
        
        for i in range(len(combined)-1,-1,-1):
            
            t = (target - combined[i][0]) / combined[i][1]
            stack.append((combined[i][0], combined[i][1], t))
            
            try:
                if stack[-1][2] <= stack[-2][2]:
                    stack.pop()
            except IndexError:
                pass
            
        print(stack)
        
        return len(stack)

if __name__ == "__main__":
    
    target = 100
    position = [0,2,4]
    speed = [4,2,1]
    """
    target = int(input())
    position = []
    speed = []
    
    while True:
        try:
            position.append(int(input()))
        except ValueError:
            break
    
    while True:
        try:
            speed.append(int(input()))
        except ValueError:
            break
    """
    s = Solution()
    
    print(s.carFleet(target, position, speed))