import sys

if len(sys.argv) < 3:
	print "2 params required."
	exit(1)

fV = sys.argv[1]
sV = sys.argv[2]
fV, sV = sV, fV

print "{}, {}".format(fV, sV)
