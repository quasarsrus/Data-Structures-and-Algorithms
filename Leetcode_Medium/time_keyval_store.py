# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 20:09:59 2024

@author: apujari1
"""

#Time Based Key-Value Store

class TimeMap:

    def __init__(self):

      self.dictionary = {}
      self.timestamp = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:

      self.dictionary[key,timestamp] = value
      if key in self.timestamp.keys(): 
        self.timestamp[key].append(timestamp)
      else:
        self.timestamp[key] = [timestamp]

    def get(self, key: str, timestamp: int) -> str:
        
      if key not in self.timestamp.keys():
        return ""

      elif timestamp < self.timestamp[key][0]:
        return ""

      elif (key,timestamp) in self.dictionary.keys():
        return self.dictionary[key, timestamp]

      else:
        left = 0
        right = len(self.timestamp[key])-1
        temp = 0
        
        while left <= right:
          
          if self.timestamp[key][(left+right)//2] > timestamp:
            right = (left+right)//2 - 1
            temp = self.timestamp[key][(left+right)//2]      
          else:          
            left = (left+right)//2 + 1
            temp = self.timestamp[key][(left+right)//2]
          
 
        return self.dictionary[key, temp]