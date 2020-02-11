from versionCheck import versionCheck
versionCheck()

from getLine import getLine
from parseLine import parseLine

def pyshell():
	while True:
		line = getLine("pyshell -> ")
		lines = line.split(";")
		for line in lines:
			parseLine(line)

if __name__ == "__main__":
	pyshell()