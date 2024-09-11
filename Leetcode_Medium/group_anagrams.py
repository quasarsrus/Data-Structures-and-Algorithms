# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 19:56:58 2024

@author: apujari1
"""

# Group Anagrams


class Solution:
    def groupAnagrams(self, strs):
        
        a = {}
        
        for i in range(len(strs)):    
            count = [0] * 26
            for j in strs[i]:
                count[ord(j)-ord('a')] += 1
                
            if tuple(count) not in a.keys():
                a[tuple(count)] = [strs[i]]
            else:
                a[tuple(count)].extend([strs[i]])

        result = []
        
        for i in a.keys():
            result.append(a[i])
        
        return result

if __name__ == "__main__":
    
    input_list = []
    
    while True:
        input_list.append(input())
        if input_list[-1] == '1':
            del input_list[-1]
            break
    
    s = Solution()
    
    print(s.groupAnagrams(input_list))