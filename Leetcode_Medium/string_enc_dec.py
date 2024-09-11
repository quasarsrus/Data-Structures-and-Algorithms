# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 19:59:50 2024

@author: apujari1
"""

#String encode and decode

class Solution:

  def encode(self,strs:list[str]) -> str:
    k = 0
    for i in strs:
      if k != 0:
        k = k + str(len(i)) + ":" + i
      else:
        k = str(len(i)) + ":" + i
    return k

  def decode(self,string:str) -> list[str]:

    dec = []
    x = 0
    while x < len(string):
        p = 0
        dum = 0
        l = x+2
        while p < int(string[x]):
          if dum != 0:
            dum = dum + string[l]
          else:
            dum = string[l]
          l += 1
          p += 1
        x = l
        dec.append(dum)
    return dec

if __name__=="__main__":
  strs = ["lint","co4:de","love","you","5:5:","42fd6:"]

  s = Solution()

  print(s.encode(strs))
  print(s.decode(s.encode(strs)))
  
  
"""
#Different solution

class solution:
    
    def __init__(self):
        
        self.string = ""
    
    def encode(self, strs):
        
        for i in strs:
            self.string = self.string + ":" + str(len(i)) + i
                
        return self
        
    
    def decode(self):
        
        ret_list = []
        temp = ""
        i = 0
        while i < len(self.string):
            temp = temp + self.string[i]
            
            if temp[0] == ":" and len(temp) == 2:             
                a = int(temp[1])           
                temp = ""
                
                for j in range(1,a+1,1):         
                    temp = temp + self.string[i + j]
                    
                ret_list.append(temp)
                temp = ""
                i = i + a      
            i += 1
        
        return ret_list
                
        
    
if __name__ == "__main__":
    
    strs = ["lint","co4:de","love","you","5:5:","42fd6:"]
    
    s = solution()
    
    print(strs == s.encode(strs).decode())
"""
