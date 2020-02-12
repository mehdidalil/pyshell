import os

def unsetenv(args):
	try:
		del os.environ[args[0]]
	except:
		return 1
	return 0