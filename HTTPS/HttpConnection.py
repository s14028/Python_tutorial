from UserAut import User
import requests, io

class HttpClient:
	def __init__(self, user):
		self.user = user
		self.connection = None

	def session(self):
		self.connection = requests.Session()
		self.connection.auth = (self.user.name, self.user.password)

	def getHTML(self, url):
		anwser = self.connection.get(url)
		return anwser.text

	@staticmethod
	def saveHtml(url, path):
		anwser = requests.get(url)
		with open(path, "a") as file:
			file.write(anwser.text.encode("utf-8").strip())
