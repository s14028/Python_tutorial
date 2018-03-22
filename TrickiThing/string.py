empty = ""

#add smth to string

empty.join(" another string")

array = [1, 2]
'''Takes positional arguments
that's why i need to tell, that array should be taken as arguments'''
f = "{} value {}".format(*array)

print(f)

print("Found {}".format(f.index("value")))

try:
	print("Didn't {}".format(f.index("Fork.")))
except:
	print("Be careful.")

wantReplace = 'abc'
wantReplace = [ord(i) for i in wantReplace]
withReplace = 'der'

w = dict(zip(wantReplace, withReplace))
string = "absadabcd"
print(str.translate(string, w))

print(string.split("d"))
