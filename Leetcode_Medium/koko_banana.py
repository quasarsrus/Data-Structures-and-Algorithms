# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 20:02:59 2024

@author: apujari1
"""

#Koko eats banana

class Solution:
    def minEatingSpeed(self, piles, h):
        
        i = 1
        while True:
            j = 0
            hours = 0
            while j < len(piles):
                hours += int(piles[j]/i)+1
                print(hours,i)
                j += 1
            if hours > h:
                i += 1
            else:
                break
            
        return i
            
            
            
                    


if __name__ == "__main__":
    
    #piles = [3,6,7,11]
    #h = 8
    piles = [30,11,23,4,20]
    h = 5
    
    s = Solution()
    
    print(s.minEatingSpeed(piles,h))