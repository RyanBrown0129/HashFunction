import os #only needed for listdir
from BitVector import * #imports BitVector, the most important part of this
userInp = input("enter in a full directory path:\n") #user inputs the full directory path
directory = os.listdir(userInp) #gets a list of all file names in the directory the user specified
output = open('output.txt','w') #opens a file to write hash hex codes to
for name in directory: #iterates through each file found
  file = BitVector(filename = userInp + '\\' + name) #since listdir only returns the file names it says file doesn't exist without including the path here
  hash = BitVector(size = 32) #32bit hash variable
  while(file.more_to_read): #while there is something more to read
    readBits = file.read_bits_from_file(8) #reads 8 bits/1 byte
    hash[0:8] = readBits ^ hash[0:8] # reads the rightmost byte
    hash << 8 #shifts 8 bits
  output.write(name + ' ' + hash.getHexStringFromBitVector() + '\n') #writes to the output file