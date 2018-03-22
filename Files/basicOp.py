import sys
import os

directoryPath = sys.argv[1]
directoryNext = sys.argv[2]
filePath = sys.argv[3]
fileNext = sys.argv[4]

os.rmdir(directoryPath)
os.remove(filePath)
os.rename(fileNext, "file")
print(os.getcwd())
os.mkdir("dir")

os.listdir(directoryNext)
condition = os.path.isdir(directoryNext)
condition = os.path.isfile(fileNext)
