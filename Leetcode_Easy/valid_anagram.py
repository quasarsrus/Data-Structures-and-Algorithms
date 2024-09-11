# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 19:53:58 2024

@author: apujari1
"""

# Valid Anagram

class Solution:
    def isAna(self, s, t) -> bool:      
        if len(s) != len(t):
            return False
        else:
            a = {}
            b = {}
            
            for i in range(len(s)):
                
                if s[i] not in a.keys():
                    a[s[i]] = 1
                else:
                    a[s[i]] += 1
                    
                if t[i] not in b.keys():
                    b[t[i]] = 1
                else:
                    b[t[i]] += 1
                
            if a == b:
                return True
            else:
                return False
        
        
if __name__ == "__main__":
    a = str(input())
    b = str(input())
    
    s = Solution()
    
    print(s.isAna(a,b))