from UserAut import User
from HttpConnection import HttpClient
import sys, io

class HTMLParses:
	def __init__(self, epxr):
		self.expt = expr


def main():
	user = User(sys.argv[1], sys.argv[2])
	client = HttpClient(user)
	client.session()
	file = open(sys.argv[3])
	httpSite = file.read()
	file.close()
	print "WWW -> {}".format(httpSite)
	HttpClient.saveHtml(httpSite, sys.argv[4])
	
if __name__ == "__main__":
	main()
