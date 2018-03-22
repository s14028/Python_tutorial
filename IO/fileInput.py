import io
import sys

fileName = sys.argv[1]
extract = open(fileName, "r") #r, w, a
print extract.read() #read the whole file and stores String
print extract.readlines() #read the whole file and stores it as array of lines
print extract.read(15) #read first 15 characters
print extract.readline() #reads a line
print extract.readline(1) #reads first line
extract.close()
