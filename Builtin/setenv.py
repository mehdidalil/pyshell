import os
from .env import env

def setenv(args):
	value = "" if len(args) <= 1 else args[1]
	if len(args) > 2:
		raise Exception("Too much arguments")
	elif len(args) == 0:
		return env([])
	try:
		os.environ[args[0]] = value
	except:
		return 1
	return 0