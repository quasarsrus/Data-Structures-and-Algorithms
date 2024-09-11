# Ashish Pujari

''' Imports modules'''

import sys
import struct

'''
Input file is accepted through a command line argument. 
This function opens the binary file and reads the contents onto a variable.

Further more, a string reads the name of the file until the extension.
For eg: 
    sys.argv[1] = input1.lzw
    encoded_file = input1
'''

with open(sys.argv[1],'br') as file1:
    lo = file1.read()
    k=0
    encoded_file = ''
    while not (ord(sys.argv[1][k])==46):
        encoded_file = encoded_file + sys.argv[1][k]
        k+=1
    file1.close()
    pass
    
if __name__ == "__main__":
    
    ''' 
    Initialises lists 
    and accepts argument for table size through command line
    '''
    
    N = int(sys.argv[2])
    max_table = 2**N
    dict_list = []
    output = []
    
    '''Populates the list with 256 unique ASCII characters'''
    
    for i in range(256):
      dict_list.append(chr(i))
      
    '''
     Computes the length of input data. Number of binary codes present 
     would be half the length since each LZW encoded code was saved 
     in 2 bytes format.
     
    '''
     
    dec = '>'
    for i in range(int(len(lo)/2)):
        dec = dec+'H' 
        
    ''' Decodes the binary codes into integer codes'''
    
    encoded_val = struct.unpack(dec, lo)
    
    '''
    Performs LZW Decoding Operation. The following block is a representation
    of the algorithm provided.
    '''
    
    code = encoded_val[0]  
    string = dict_list[code]
    print(string)
    output.append(string)
    for k in range(len(encoded_val)-1):
        code = encoded_val[k+1]
        if code>(len(dict_list)-1):
            new_string = string+string[0]
        else:
            new_string = dict_list[code]
        print(new_string)
        output.append(new_string)
        if len(dict_list) < max_table:
            dict_list.append(string+new_string[0])
        string = new_string
        
    '''
    This function opens a file 
    and writes the decoded codes to it.

    The file name is derived from the concatenation 
    of the string encoded_file and the string literal '_decoded.txt'.
    '''
    
    with open(encoded_file+'_decoded.txt','w') as fo1:
        for i in output:
            fo1.write(i)
        fo1.close()
        pass

        
    
    