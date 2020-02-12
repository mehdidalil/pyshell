from Builtin import Builtin
from Exec import Exec

def parseLine(line):
	line = line.split()
	proc = Builtin(line)
	ret = proc.run()
	if ret == None:
		proc = Exec(line)
		ret = proc.run()