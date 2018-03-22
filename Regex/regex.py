import sys
import re
whatToSearch = sys.argv[1]

for i in sys.argv[2:]:
	find = re.search(whatToSearch, i)
	if find != None:
		print(find.group(0))
	print("")
	for w in re.finditer(whatToSearch, i):
		print(w.group(0))

for i in re.findinter(whatToSearch, sys.argv[2:]):
	index = i.span()
regex = re.compile(whatToSearch)

print(regex.sub("", sys.argv[3]))
