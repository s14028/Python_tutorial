import io
import sys

with open(sys.argv[1], "w") as extract:
	extract.write("Message\n") #write creates a new file, because we are using w option.
	extract.writelines(["Some", " banch", " text"]) #read the whole file and stores it as array of lines.
