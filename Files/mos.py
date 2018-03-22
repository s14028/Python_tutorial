import os
os.chdir("../")
for dirName, dirList, fileList in os.walk("."):
	print(dirName)
	print(dirList)
	print(fileList)
	print()
