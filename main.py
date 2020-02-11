import sys

if __name__ == "__main__":
	if sys.version_info[0] < 3:
		print("Python 3 or a more recent version is required.")
		exit()

from parseLine import parseLine
from Exec import Exec
from Builtin import Builtin

def main():
	while True:
		tab = parseLine("pyshell -> ")
		proc = Builtin(tab)
		ret = proc.run()
		if ret == None:
			proc = Exec(tab)
			ret = proc.run()

if __name__ == "__main__":
	main()