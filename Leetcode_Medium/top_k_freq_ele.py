# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 19:57:28 2024

@author: apujari1
"""

# Top K Frequent Elements

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        counter = {}
        
        for i in nums:
            if i not in counter.keys():
                counter[i] = 1
            else:
                counter[i] += 1
        
        counter2 = {}
        
        for i in counter.keys():
            if counter[i] not in counter2.keys():
                counter2[counter[i]] = [i]
            else:
                counter2[counter[i]].append(i)
                
        return_list2 = []
        j = 0
        while(j < k):
            try:
                temp = counter2[max(counter2.keys())]
                for i in temp:
                    return_list2.append(i)
                    j += 1
                
                counter2.pop(max(counter2.keys())) 
            except ValueError:
                continue
        
        return return_list2

if __name__ == "__main__":
    
    input_list = [4,1,-1,2,-1,2,3]
    int_k = 2

    s = Solution()
    
    print(s.topKFrequent(input_list,int_k))