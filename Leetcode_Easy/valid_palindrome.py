# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 19:55:18 2024

@author: apujari1
"""

#Valid Palindrome

class Solution:
  def isPalindrome(self, string: str) -> bool:

    if string == " ":
      return True

    val_num = set(range(ord('0'),ord('9')+1))
    val_alph = set(range(ord('a'),ord('z')+1))
    val_Alph = set(range(ord('A'),ord('Z')+1))
    new_string = str()

    for i in string:

      if ord(i) in val_num.union(val_alph):
        new_string = new_string + i

      elif ord(i) in val_Alph:
        new_string = new_string + chr(ord(i)+32)

      else:
        continue

    print(new_string)

    i = 0
    j = len(new_string)-1

    while i<=j:
      if new_string[i] != new_string[j]:
        return False

      i += 1
      j -= 1

    return True

if __name__=="__main__":

  string = "A man, a plan, a canal: Panama"
  s = Solution()

  print(s.isPalindrome(string))