# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 19:47:18 2024

@author: apujari1
"""

# Roman Numerals

a = dict();

a["I"] = 1;
a["V"] = 5;
a["X"] = 10;
a["L"] = 50;
a["C"] = 100;
a["D"] = 500;
a["M"] = 1000;

l = str(input());
b = 0

j = 0

while j < len(l)-1:
    
    if a[l[j]] >= a[l[j+1]] :
        
        b = b + a[l[j]]
        j += 1
    else:
        b = b + (a[l[j+1]] - a[l[j]])
        j += 2
    print(j)
if j < len(l):
    b += a[l[j]]
        
print(b);