'''
Purpose:
You are having function, which has bottleneck at some point (db connection), and then is asks for arguments
to deal with bottleneck.
Sometimes you couldn't provide the whole data once. That's why the coprograms used.
'''

def dbConnectivity():
	'''
	with connect() as db:
	'''
	while True:
		input = (yield)
		print(input)
generator = dbConnectivity()

next(generator)
generator.send("Text.")
generator.close()
