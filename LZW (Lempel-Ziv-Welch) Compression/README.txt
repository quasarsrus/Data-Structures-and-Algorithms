Ashish Pujari

LZW Compression Algorithm (Encoding and Decoding)

Language-> Python 3.5

  The files 'encoding.py' and 'decoding.py' perform LZW compression on a set of strings and decodes the compressed string to its original form, respectively.

Running Instruction:

  To run 'encoding.py', type the following command in your python command prompt: path>python encoding.py [Input text File]* [Bit Length Integer]**
  (* -> example file name of the form input1.txt, ** -> Integer bit length can usually be 12)

  Similarly, to run 'decoding.py', type the following command in your python command prompt: path>python decoding.py [Input LZW File]# [Bit Length Integer]##
  (# -> example file name of the form input1.lzw, ## -> Integer bit length can usually be 12)

Expected Operation:

  The code attached works perfectly for various combination of characters. encoding.py accepts a string set from a file whose name is [input_name].txt
  and outputs a binary file of the name [input_name].lzw. 

  One can now use [input_name].lzw as an input for decoding.py that will output the decoded string set in the form of [input_name]_decoded.txt. 

  To test the codes, the files input1.txt and input2.txt were used(provided as an example) and the resulting output files turned out to be exactly 
  like the output files provided(input1.lzw, input2.lzw, input1_decoded.txt, and input2_decoded.txt).

  To confirm the accuracy of this program, two more customised input files(input3.txt and input4.txt) were created. The final output from the decoder matched
  the input, hence verifying the accuracy of this program. Those files, along with their outputs, are added in the examples folder.

Program Design:

  encoder.py reads a '.txt' file and ultimately ouputs a binary file as '.lzw'. The algorithm was already provided so the only unique aspect was 
  comparing the element with an existing key in the dictionary. A function that employs the basic notion of screening through the list via a while loop
  until the desired index is found (and returned). This function is designed in a way that keeps in mind that it will only be called 
  when the value is in the list.  
  
  decoder.py reads a '.lzw' binary file and ultimately outputs the decoded '.txt' file. The unique aspect in this file is its usage of the 'struct' module 
  to unpack the encoded values from binary form to integer values. Since encoded.py saves each integer value as 2 bytes (16-bit form), the number of bytes 
  helps in figuring out the resulting number of integer codes (it should be the half of it).

  The dictionary in both cases is a list of 256 unique characters that are appended in the same sequential order as the ASCII table. 

  