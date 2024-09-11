# Ashish Pujari

''' Imports modules'''

import sys

''' 
The fucntion index_list(,) accepts a string and a list to compare whether 
such a symbol exists within the list.
It returns the index corresponding to its location in the list.

(Only called when the symbol exists in the list)
''' 

def index_list(a,l):
    p = 0
    while not (a==l[p]):
        p+=1
    return p 
    
  #output = [p for p,q in enumerate(l) if a==q]
  #return output[0]

'''
Input file is accepted through a command line argument. 
This function opens the file and reads the contents onto a variable.

Further more, a string reads the name of the file until the extension.
For eg: 
    sys.argv[1] = input1.txt
    input_file = input1
'''

with open(sys.argv[1],'r') as file:
    re = file.read()
    k=0
    input_file = ''
    while not (ord(sys.argv[1][k])==46):
        input_file = input_file + sys.argv[1][k]
        k+=1
    file.close()
    pass

if __name__ == "__main__":
    
    ''' 
    Initialises lists 
    and accepts argument for table size through command line
    '''
    N = int(sys.argv[2])
    max_table = 2**N
    string = ""
    dict_list = []
    lo = []
    
    '''Populates the list with 256 unique ASCII characters'''
    
    for i in range(256):
      dict_list.append(chr(i))
      
    '''
    Performs LZW Encoding Operation. The following block is a representation
    of the algorithm provided.
    '''
    
    for i in range(len(re)):
      symbol = re[i]
      if (string+symbol) in dict_list:
        string = string+symbol
      else:
        code = index_list(string,dict_list) #Gets index of the string in the list
        print(code)
        if len(dict_list) < max_table:
          dict_list.append((string+symbol))
        lo.append(code.to_bytes(2,'big')) #Appends codes into a new list as bytes
        string=symbol
    code = index_list(string,dict_list)
    print(code)
    lo.append(code.to_bytes(2,'big'))
    
    
    
    '''
    This function opens a binary file 
    and writes the codes, converted to 2 bytes each, to it.

    The file name is derived from the concatenation 
    of the string input_file and the string literal '.lzw'.
    '''
    
    with open(input_file+'.lzw','bw') as fo:
        for i in lo:
            fo.write(i)
        fo.close()
        pass
