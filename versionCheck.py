import sys

def versionCheck():
	if sys.version_info[0] < 3:
		print("Python 3 or a more recent version is required.")
		exit()