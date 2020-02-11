import os
from stat import S_ISDIR

def parseDirectory(pwd, dir):
	pwdList = list(filter(None, pwd.split('/')))
	dir = list(filter(None, dir.split('/')))
	for i in dir:
		if i == "..":
			if pwdList:
				pwdList.pop()
		elif i == ".":
			pass
		else:
			pwdList.append(i)
	path = "/"
	for i in pwdList:
		path += i + "/"
	return path

def cd(args):
	pwd = os.getenv("PWD")
	mode = 0
	if pwd == None:
		raise Exception("Term variable PWD not set")
	if len(args) > 1:
		raise Exception("Too much arguments")
	try:
		os.stat(pwd)
	except:
		raise Exception("PWD not valid")
	try:
		mode = os.stat(args[0]).st_mode
	except:
		raise Exception("No such directory")
	if not S_ISDIR(mode):
		raise Exception("Not a directory")
	newDir = args[0] if args[0].startswith("/") else parseDirectory(pwd, args[0])
	try:
		os.chdir(newDir)
		os.environ["PWD"] = newDir
	except:
		raise Exception("chdir fail")
	return 0