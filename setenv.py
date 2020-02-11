import os

def setenv(args):
	value = "" if len(args) <= 1 else args[1]
	try:
		os.environ[args[0]] = value
	except:
		return 1
	return 0