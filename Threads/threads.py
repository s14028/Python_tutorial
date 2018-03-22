import threading
shared_lock = threading.Lock()
semaphore = threading.Semaphore(1)
def section(i):
	shared_lock.acquire()
	print "CSection. {}".format("Section.")
	shared_lock.release()
	with shared_lock:
		print "Some thread {}".format(i)
def main():
	f = threading.Thread(target = section, args = (0,))
	l = threading.Thread(target = section, args = (1,))
	f.start()
	l.start()
	#Not necessary
	f.join()
	l.join()
if __name__ == "__main__":
	main()
